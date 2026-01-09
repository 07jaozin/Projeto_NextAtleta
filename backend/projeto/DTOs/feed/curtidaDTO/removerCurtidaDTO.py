class RemoverCurtidaDTO:
    """
    DTO responsável por validar os dados
    para remoção (soft delete) de uma curtida.
    """

    def __init__(self, data: dict):
        self.data = data
        self.data_final = {}

    def validar(self):
        if not self.data:
            raise ValueError("Dados para remoção da curtida não enviados")

        curtida_id = self.data.get("curtida_id")

        if not curtida_id:
            raise ValueError("ID da curtida é obrigatório")

        self.data_final["curtida_id"] = int(curtida_id)

    def build(self):
        return self.data_final