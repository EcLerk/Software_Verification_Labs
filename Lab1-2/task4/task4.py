import os
import webbrowser


def create_html(n):

    step = float(255 / n)
    html = [f'<!DOCTYPE html>',
                f'<html>',
                f'<body>',
                f'<table cellspacing="0" cellpadding="0" style="width: 700px;">']


    for i in range(n):
        color = int(255 - i * step)
        html.append(
            f'<tr style="height: 10px; border: none; background-color: rgb({color}, {color}, {color})"><td></td></tr>'
        )

    html.append(f'</table>')
    html.append(f'</body>')
    html.append(f'</html>')

    return '\n'.join(html)


def main():
    n = 70
    filename = "my_file.html"
    with open(filename, "w") as f:
        f.write(create_html(n))

    # Открываем файл в браузере
    absolute_path = os.path.abspath(filename)
    webbrowser.open("file://" + absolute_path)


if __name__ == "__main__":
    main()