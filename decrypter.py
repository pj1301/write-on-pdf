import pikepdf as pikepdf

def decrypt_file(file):
  path_list = file.name.split("/")[0:-1]
  path = "/".join(path_list).strip()
  filename = file.name.split("/")[-1]

  new_file_name = "decrypted_" + filename
  new_file_path = path + "/" + new_file_name

  with pikepdf.open(file.name) as pdf:
    pdf.save(new_file_path)
    print('Operation completed')
