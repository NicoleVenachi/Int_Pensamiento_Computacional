def busca_pais(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    """

    try:
        return paises[pais]
    except KeyError:
        return None

#  JS, paradgma LBYL
# function buscaPais(paises, pais) {
#   if(!Object.keys(paises).includes(pais)) {
#     return null;
#   }
#
#   return paises[pais];
# }
