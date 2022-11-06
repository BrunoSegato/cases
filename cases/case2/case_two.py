import io
import os
from pathlib import Path


class CaseTwo:

    @staticmethod
    def add_break_line(line: str):
        if line.find('\n') == -1:
            line += '\n'
        return line

    def last_lines(self, file_name: str, buffer_size: int = io.DEFAULT_BUFFER_SIZE):
        with open(Path(file_name)) as handler:
            offset = 0
            segment = None
            handler.seek(0, os.SEEK_END)
            file_size = remaining_size = handler.tell()
            while remaining_size > 0:
                offset = min(file_size, offset + buffer_size)
                handler.seek(file_size - offset)
                buffer = handler.read(min(remaining_size, buffer_size))
                remaining_size -= buffer_size
                lines = buffer.split('\n')
                if segment is not None:
                    if buffer[-1] != '\n':
                        lines[-1] += segment
                    else:
                        yield print(self.add_break_line(segment), end='')
                segment = lines[0]
                for index in range(len(lines) - 1, 0, -1):
                    if lines[index]:
                        yield print(self.add_break_line(lines[index]), end='')
            if segment is not None:
                yield print(self.add_break_line(segment), end='')
