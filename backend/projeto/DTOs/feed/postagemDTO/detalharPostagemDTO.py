class DetalharPostagemDTO:
    """
    DTO responsável por estruturar os dados completos
    de uma postagem específica.
    """

    def __init__(self, postagem):
        self.postagem = postagem

    def build(self):
        return {
            "id": self.postagem.id,
            "conteudo": self.postagem.conteudo,
            "legenda": self.postagem.legenda,
            "created_at": (
                self.postagem.created_at.isoformat()
                if self.postagem.created_at else None
            ),
            "ativo": self.postagem.ativo,

            "usuario": {
                "id": self.postagem.usuario.id if self.postagem.usuario else None,
                "nome": self.postagem.usuario.nome if self.postagem.usuario else None,
                "foto": self.postagem.usuario.foto if self.postagem.usuario else None,
            },

            "quantidade_curtidas": len(self.postagem.curtidas),

            "quantidade_comentarios": len(self.postagem.comentarios),

            "comentarios": [
                {
                    "id": comentario.id,
                    "conteudo": comentario.conteudo,
                    "usuario_id": comentario.usuario_id,
                    "nome_usuario": comentario.usuario.nome if comentario.usuario else None,
                    "foto_usuario": comentario.usuario.foto_perfil if comentario.usuario else None,
                    "created_at": (
                        comentario.created_at.isoformat()
                        if comentario.created_at else None
                    ),
                }
                for comentario in self.postagem.comentarios
                if comentario.ativo
            ]
        }