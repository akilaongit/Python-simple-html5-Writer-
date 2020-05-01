html_name = input("Enter name of html file: ")
css_name = input("Enter name if css file(press enter if it is none): ")
js_name = input("Enter name if javascript file(press enter if it is none): ")

html_file = open(f'{html_name}.html','w+')

if css_name == '':
    pass

else:
    css_file = open(f'{css_name}.css', 'w+')

if js_name == '':
    pass

else:
    js_file = open(f'{js_name}.js', 'w+')

site_title = input("Enter title of the site: ")
site_heading = input("Enter heading of the site: ")
site_paragraph = input("Enter paragraph for your site: ")
site_comment = input("Enter comment for your site: ")

html_file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_title}</title>
</head>
<body>
   <h1>{site_heading}</h1>
   <p>{site_paragraph}</p>
</body>
</html>
""")
