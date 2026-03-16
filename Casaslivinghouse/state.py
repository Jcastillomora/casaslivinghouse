import reflex as rx
import pandas as pd
from .models import Casa

EXCEL_PATH = "assets/Catálogo .xlsx"
EXCEL_SHEET = "Hoja 1"


class State(rx.State):
    """Estado global de la aplicación."""

    casas: list[Casa] = []
    total_casas: int = 0
    is_loading: bool = False
    data_loaded: bool = False

    search_term_casas: str = ""
    current_casa_id: str = ""
    min_superficie: int = 18
    max_superficie: int = 137
    min_precio: int = 1000000
    max_precio: int = 7000000
    selected_dormitorios: list[int] = []
    selected_banos: list[int] = []
    all_dormitorios: list[int] = []
    all_banos: list[int] = []

    def load_casas(self):
        """Carga las casas desde Excel (solo una vez por sesión)."""
        if self.data_loaded:
            return

        self.is_loading = True
        yield  # Permite que el frontend muestre el estado de carga

        try:
            df = pd.read_excel(
                EXCEL_PATH,
                sheet_name=EXCEL_SHEET,
                engine="openpyxl",
                dtype={
                    "id": "int64",
                    "modelo": "string",
                    "superficie(m2)": "int64",
                    "dormitorios": "int64",
                    "baños": "int64",
                    "descripción": "string",
                    "imagen": "string",
                    "url_imagen": "string",
                    "plano": "string",
                },
            )

            df = df.replace("", None)
            df = df.dropna(subset=["id"])
            df["id"] = pd.to_numeric(df["id"], errors="coerce")
            df = df.dropna(subset=["id"])
            df["id"] = df["id"].astype(int)

            df = df.rename(
                columns={
                    "superficie(m2)": "superficie_m2",
                    "baños": "banos",
                    "descripción": "descripcion",
                }
            )

            df["modelo"] = (
                df["modelo"].fillna("Modelo desconocido").replace("nan", "Modelo desconocido")
            )
            df["superficie_m2"] = (
                pd.to_numeric(df["superficie_m2"], errors="coerce").fillna(0).astype(int)
            )
            df["dormitorios"] = (
                pd.to_numeric(df["dormitorios"], errors="coerce").fillna(1).astype(int)
            )
            df["banos"] = (
                pd.to_numeric(df["banos"], errors="coerce").fillna(1).astype(int)
            )

            def clean_precio(precio):
                if pd.isna(precio) or precio == "":
                    return 0
                precio_str = str(precio)
                precio_limpio = (
                    precio_str.replace("$", "")
                    .replace(".", "")
                    .replace(",", "")
                    .replace(" ", "")
                )
                try:
                    return int(float(precio_limpio))
                except (ValueError, TypeError):
                    return 0

            df["precio"] = df["precio"].apply(clean_precio)
            df["descripcion"] = (
                df["descripcion"]
                .fillna("Sin descripción disponible")
                .replace("nan", "Sin descripción disponible")
            )
            df["imagen"] = df["imagen"].fillna("").replace("nan", "")
            df["url_imagen"] = (
                df["url_imagen"].fillna("/casa_default.jpg").replace("nan", "/casa_default.jpg")
            )
            df["plano"] = df["plano"].fillna("").replace("nan", "")

            def fmt_precio(p: int) -> str:
                if p == 0:
                    return "Consultar precio"
                return f"${p:,}".replace(",", ".")

            df["precio_texto"] = df["precio"].apply(fmt_precio)
            self.casas = [Casa(**row.to_dict()) for _, row in df.iterrows()]
            self.total_casas = len(self.casas)

            self.all_dormitorios = sorted(df["dormitorios"].dropna().unique().tolist())
            self.all_banos = sorted(df["banos"].dropna().unique().tolist())

            superficies_validas = df[df["superficie_m2"] > 0]["superficie_m2"]
            precios_validos = df[df["precio"] > 0]["precio"]

            if len(superficies_validas) > 0:
                self.min_superficie = int(superficies_validas.min())
                self.max_superficie = int(superficies_validas.max())

            if len(precios_validos) > 0:
                self.min_precio = int(precios_validos.min())
                self.max_precio = int(precios_validos.max())

            self.data_loaded = True

        except FileNotFoundError:
            print(f"❌ No se encontró el archivo Excel: {EXCEL_PATH}")
            self.casas = []
            self.total_casas = 0
            self.data_loaded = True  # Evitar reintentos infinitos
        except Exception as e:
            print(f"❌ Error cargando casas: {e}")
            self.casas = []
            self.total_casas = 0
            self.data_loaded = True
        finally:
            self.is_loading = False

    def reset_filters(self):
        """Restablece todos los filtros a sus valores originales."""
        self.search_term_casas = ""
        self.selected_dormitorios = []
        self.selected_banos = []
        if self.casas:
            superficies = [c.superficie_m2 for c in self.casas if c.superficie_m2 > 0]
            precios = [c.precio for c in self.casas if c.precio > 0]
            if superficies:
                self.min_superficie = min(superficies)
                self.max_superficie = max(superficies)
            if precios:
                self.min_precio = min(precios)
                self.max_precio = max(precios)

    def load_casa_detail(self):
        """Carga el detalle de una casa desde los parámetros de la URL."""
        self.current_casa_id = self.router.page.params.get("casa_id", "")
        if not self.data_loaded:
            yield State.load_casas

    def navigate_to_casa(self, casa_id: int):
        """Navega a la página de detalle de una casa."""
        return rx.redirect(f"/casa/{casa_id}#detalle")

    @rx.var(cache=True)
    def current_casa(self) -> Casa:
        """Retorna la casa actual según el parámetro de URL."""
        for casa in self.casas:
            if str(casa.id) == self.current_casa_id:
                return casa
        return Casa(
            id=0,
            modelo="",
            superficie_m2=0,
            dormitorios=0,
            banos=0,
            precio=0,
            precio_texto="",
            descripcion="",
            imagen="",
            url_imagen="/casa_default.jpg",
            plano="",
        )

    @rx.var(cache=True)
    def current_casa_precio_texto(self) -> str:
        """Precio de la casa actual formateado en formato chileno."""
        precio = self.current_casa.precio
        if precio == 0:
            return "Consultar precio"
        return f"${precio:,}".replace(",", ".")

    @rx.var(cache=True)
    def filtered_casas(self) -> list[Casa]:
        """Filtra las casas según criterios de búsqueda (resultado cacheado)."""
        term = self.search_term_casas.lower().strip()
        filtered = self.casas

        if term:
            filtered = [
                casa
                for casa in filtered
                if (term in str(casa.id))
                or (term in casa.modelo.lower())
                or (term in casa.descripcion.lower())
            ]

        if self.selected_dormitorios:
            filtered = [
                casa for casa in filtered if casa.dormitorios in self.selected_dormitorios
            ]

        if self.selected_banos:
            filtered = [casa for casa in filtered if casa.banos in self.selected_banos]

        filtered = [
            casa
            for casa in filtered
            if self.min_superficie <= casa.superficie_m2 <= self.max_superficie
        ]

        filtered = [
            casa
            for casa in filtered
            if self.min_precio <= casa.precio <= self.max_precio
        ]

        return filtered

    @rx.var(cache=True)
    def filtered_casas_count(self) -> int:
        """Número de casas que coinciden con los filtros actuales."""
        return len(self.filtered_casas)
