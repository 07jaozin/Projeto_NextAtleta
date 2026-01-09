class AtualizarComentarioDTO:
    """
    DTO responsável por validar e preparar os dados
    para atualização de um comentário.
    """

    CAMPOS_PERMITIDOS = {
        "conteudo"
    }

    def __init__(self, data: dict):
        self.data = {
            k: v for k, v in data.items()
            if k in self.CAMPOS_PERMITIDOS
        }

    def validar(self):
        if not self.data:
            raise ValueError("Nenhum dado válido para atualização do comentário")

    def build(self):
        return self.data