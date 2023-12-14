""" 3) Dado o seguinte objeto:"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Agrupa elementos por dicionário.'

    def handle(self, *args, **kwargs):
        objeto = [{
            "message_tag": "TEMPERATURE_MIN",
            "element_dictionary": "INMET",
            "element": "MIN_AIR_TEMP_2M_C"
        }, {
            "message_tag": "RELATIVE_HUMIDITY_MIN",
            "element_dictionary": "INMET",
            "element": "MIN_REL_HUMIDITY_2M_PCT"
        }, {
            "message_tag": "temperature",
            "element": "AVG_AIR_TEMP_2M_C",
            "element_dictionary": "METAR"
        }, {
            "message_tag": "PrecMin",
            "element_dictionary": "SIMEPAR_MET",
            "element": "DISCARDED",
        }, {
            "message_tag": "Prec",
            "element_dictionary": "SIMEPAR_MET",
            "element": "ACCUM_PRECIP_2M_MM",
        }]

        resultado = self.agrupar_elementos_por_dicionario(objeto)
        self.stdout.write(self.style.SUCCESS(str(resultado)))

    def agrupar_elementos_por_dicionario(self, objeto):
        resultado = {}

        for item in objeto:
            dicionario = item['element_dictionary']
            elemento = item['element']

            resultado.setdefault(dicionario, []).append(elemento)

        return resultado
