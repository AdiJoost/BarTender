from data.dataManagers.abstracts.fileManager import FileManager
import csv

class CSVManager(FileManager):

    FILE_TYPE: str = ".csv"

    def __init__(self, header: list, filename, folderpath: str,) -> None:
        super().__init__(filename, folderpath, self.FILE_TYPE)
        self.header = header

    def initFile(self) -> None:
        with open(self.absolutPath, "w", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.header)
