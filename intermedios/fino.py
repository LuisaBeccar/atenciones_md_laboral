
import pandas as pd
import numpy as np
install spacy
#pip install catboost
#uname
from sklearn.feature_extraction.text import CountVectorizer
install spacy
spacy download es_core_news_sm
import spacy
sp = spacy.load('es_core_news_sm')


# ----------------------
class AtencionAnalyzer:
    def __init__(self, text, stop_words):
        self.text = text
        self.stop_words = stop_words
        self.rows = self._prepare_data()
        self.data1 = None
        self.data2 = None

    def _prepare_data(self):
        """Divide el texto en filas de 100 palabras."""
        p = 100  # Número de palabras por fila
        words = self.text.split()
        rows = []
        for i in range(0, len(words), p):
            rows.append(' '.join(words[i:i+p]))
        return pd.Series(rows)

    def _count_unigrams(self):
        """Cuenta las palabras individuales (unigramas)."""
        counter1 = CountVectorizer(stop_words=self.stop_words)
        X_t1 = counter1.fit_transform(self.rows)
        self.data1 = pd.DataFrame(X_t1.toarray().sum(axis=0),
                                  index=counter1.get_feature_names_out(),
                                  columns=['freq'])

    def _count_bigrams(self):
        """Cuenta las combinaciones de dos palabras (bipalambras)."""
        counter2 = CountVectorizer(ngram_range=(2, 2))
        X_t2 = counter2.fit_transform(self.rows)
        self.data2 = pd.DataFrame(X_t2.toarray().sum(axis=0),
                                  index=counter2.get_feature_names_out(),
                                  columns=['freq']).sort_values('freq', ascending=False)

    def analyze(self):
        """Realiza el análisis de atenciones virtuales y presenciales."""
        self._count_unigrams()
        self._count_bigrams()

        virtuales = self._count_virtuales()
        presenciales = self._count_presenciales()

        print("Asistencias virtuales:", virtuales)
        print("\n---------------------------------------")
        print("Asistencias presenciales:", presenciales)

    def _count_virtuales(self):
        """Cuenta las asistencias virtuales."""
        return (self.data2.query('index == "recibo certificado"').sum() + 
                self.data2.query('index == "recibo certificados"').sum() +
                self.data2.query('index == "recibo certif"').sum() +  
                self.data2.query('index == "se recibe"').sum() + 
                self.data2.query('index == "envia certif"').sum() +
                self.data2.query('index == "envia certificado"').sum() + 
                self.data2.query('index == "envia certificados"').sum() + 
                self.data2.query('index == "envia constancia"').sum() +
                self.data2.query('index == "recibo mail"').sum() + 
                self.data2.query('index == "recibo aviso"').sum() + 
                self.data2.query('index == "se comunica"').sum() + 
                self.data2.query('index == "sector informa"').sum() + 
                self.data2.query('index == "me comunico"').sum() + 
                self.data1.query('index == "llamo"').sum() +
                self.data2.query('index == "intento comunicarme"').sum())

    def _count_presenciales(self):
        """Cuenta las asistencias presenciales."""
        return (self.data1.query('index == "concurre"').sum() +
                self.data1.query('index == "concurrio"').sum() +
                self.data1.query('index == "acude"').sum() + 
                self.data1.query('index == "acudió"').sum() +
                self.data2.query('index == "se presenta"').sum() +
                self.data2.query('index == "se presentó"').sum())

# Uso de la clase
if __name__ == "__main__":
    from spacy.lang.es import stop_words as es_stop_words
    text = input("Seleccione la columna a analizar, copie y pegue aquí: ")
    stop_words = list(es_stop_words.STOP_WORDS)  # Define aquí tu lista de stop words
    analyzer = AtencionAnalyzer(text, stop_words)
    analyzer.analyze()
