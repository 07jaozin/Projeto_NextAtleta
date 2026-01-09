class PostagemFeedDTO:
    """
    DTO responsável por representar uma postagem no feed.

    Usado para listagens (feed principal, perfil do usuário, etc).
    Deve ser leve e conter apenas informações necessárias
    para exibição no frontend.
    """

    def __init__(self, postagem):
        self.postagem = postagem

    def build(self):
        return {
            "id": self.postagem.id,
            "conteudo": self.postagem.conteudo,
            "legenda": self.postagem.legenda,
            "usuario_id": self.postagem.usuario_id,
            "created_at": (
                self.postagem.created_at.isoformat()
                if self.postagem.created_at
                else None
            ),
            "ativo": self.postagem.ativo,

            # Dados do usuário
            "nome_usuario": (
                self.postagem.usuario.nome
                if self.postagem.usuario
                else None
            ),
            "foto_usuario": (
                self.postagem.usuario.foto
                if self.postagem.usuario
                else None
            ),

            # Métricas
            "quantidade_curtidas": len(self.postagem.curtidas),
            "quantidade_comentarios": len(self.postagem.comentarios),
        }