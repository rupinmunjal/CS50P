def checkExtension(ext):
    if ext.endswith(".gif") == True:
        return "image/gif"
    elif ext.endswith(".jpg") == True:
        return "image/jpeg"
    elif ext.endswith(".jpeg") == True:
        return "image/jpeg"
    elif ext.endswith(".png") == True:
        return "image/png"
    elif ext.endswith(".pdf") == True:
        return "application/pdf"
    elif ext.endswith(".txt") == True:
        return "text/plain"
    elif ext.endswith(".zip") == True:
        return "application/zip"
    else:
        return "application/octet-stream"

def main():
    ext = input("File name: ").lower().strip()
    print(checkExtension(ext))

main()
