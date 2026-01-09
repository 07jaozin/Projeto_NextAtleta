from datetime import datetime

class FiltrarPostagemDTO:
    """
    DTO responsável por validar e organizar
    os filtros utilizados na listagem de postagens.
    """

    CAMPOS_PERMITIDOS = {
        "usuario_id",
        "ativo",
        "data_inicio",
        "data_fim",
        "pagina",
        "limite"
    }

    def __init__(self, params: dict):
        self.params = {
            k: v for k, v in params.items()
            if k in self.CAMPOS_PERMITIDOS
        }

    def validar(self):
        if "pagina" in self.params:
            self.params["pagina"] = int(self.params["pagina"])
            if self.params["pagina"] < 1:
                raise ValueError("Página deve ser maior que zero")

        if "limite" in self.params:
            self.params["limite"] = int(self.params["limite"])
            if self.params["limite"] < 1:
                raise ValueError("Limite deve ser maior que zero")

        if "ativo" in self.params:
            self.params["ativo"] = str(self.params["ativo"]).lower() == "true"

        if "data_inicio" in self.params:
            self.params["data_inicio"] = datetime.fromisoformat(
                self.params["data_inicio"]
            )

        if "data_fim" in self.params:
            self.params["data_fim"] = datetime.fromisoformat(
                self.params["data_fim"]
            )

    def build(self):
        return self.params