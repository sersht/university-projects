class StringHasher:
    def __init__(self, point=(10**3+7), modulo=(10**9+7)):
        self.point = point
        self.modulo = modulo

    @staticmethod
    def _standard_hash(string):
        return hash(string)

    def _polynomial_hash(self, string):
        hash_value, coefficient = 0, 1

        for i in range(1, len(string) + 1):
            hash_value += ord(string[-i]) * coefficient
            hash_value %= self.modulo

            coefficient *= self.point
            coefficient %= self.modulo

        return hash_value

    def get_hash(self, string):
        return self._polynomial_hash(string)

    def equal(self, str_a, str_b):
        if not (isinstance(str_a, str) and isinstance(str_b, str)):
            raise ValueError("Strings needed to compare")
        return self.get_hash(str_a) == self.get_hash(str_b)


class FileInteractor:
    def __init__(self, read_path, write_path):
        self.read_path = read_path
        self.write_path = write_path

    def __enter__(self):
        self.reader = open(self.read_path, encoding="utf-8")
        self.writer = open(self.write_path, mode="wt", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.reader.close()
        self.writer.close()

    def get_unit(self):
        string = str()
        while True:
            chunk = self.reader.read(1)

            if chunk == "":
                return (string, chunk)

            if chunk.isalpha():
                string += chunk
            else:
                return (string, chunk)

    def write(self, word):
        self.writer.write(word)


def get_dictionary(input_text):
    dictionary = {
        "Слово": "Замена",
    }
    return dictionary


if __name__ == "__main__":
    input_text = r"input.txt"
    output_text = r"output.txt"

    mapped = get_dictionary(input_text)

    hasher = StringHasher()
    with FileInteractor(input_text, output_text) as file_inter:
        EOF = False
        while not EOF:
            unit = file_inter.get_unit()

            word = mapped[unit[0]] if (unit[0] in mapped) else unit[0]
            symbol = unit[1]

            file_inter.write(word)
            file_inter.write(symbol)

            EOF = symbol == ""
