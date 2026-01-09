import os

class CriarPostagemDTO:
    """
    DTO responsável por validar e preparar os dados de criação de uma postagem.
    Atua como camada entre o controller e o service.
    """

    EXTENSOES_PERMITIDAS = {
        '.jpg', '.jpeg', '.png', '.mp4', '.mov'
    }

    def __init__(self, form_data: dict, files: dict, usuario_id: int):
        self.form_data = form_data
        self.files = files
        self.usuario_id = usuario_id
        self.data_final = {}

    def validar(self):
        if not self.usuario_id:
            raise ValueError("Usuário inválido")

        arquivo = self.files.get('conteudo')
        if not arquivo:
            raise ValueError("Arquivo de mídia é obrigatório")

        extensao = os.path.splitext(arquivo.filename)[1].lower()
        if extensao not in self.EXTENSOES_PERMITIDAS:
            raise ValueError(
                f"Extensão inválida ({extensao}). Permitidas: {', '.join(self.EXTENSOES_PERMITIDAS)}"
            )

    def processar(self):
        """
        Mapeia os dados recebidos para o formato final esperado pelo service/model.
        """
        self.data_final.update({
            "conteudo": self.files.get('conteudo'),
            "legenda": self.form_data.get('legenda'),
            "usuario_id": self.usuario_id
        })

    def build(self):
        return self.data_final