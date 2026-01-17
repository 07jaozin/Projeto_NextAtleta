class CriarComentarioDTO:
    """
    DTO responsável por validar e preparar os dados
    para criação de um comentário em uma postagem.
    """

    CAMPOS_OBRIGATORIOS = {
        "conteudo",
        "postagem_id"
    }

    CAMPOS_OPCIONAIS = {
        "comentario_pai_id"
    }

    def __init__(self, data: dict):
        self.data = data
        self.data_final = {}

    def validar(self):
        if not self.data:
            raise ValueError("Dados do comentário não enviados")

        for campo in self.CAMPOS_OBRIGATORIOS:
            if campo not in self.data or not self.data.get(campo):
                raise ValueError(f"Campo obrigatório ausente: {campo}")

        self.data_final["conteudo"] = self.data.get("conteudo")
        self.data_final["postagem_id"] = int(self.data.get("postagem_id"))

        comentario_pai_id = self.data.get("comentario_pai_id")
        if comentario_pai_id:
            self.data_final["comentario_pai_id"] = int(comentario_pai_id)

    def build(self):
        return self.data_final