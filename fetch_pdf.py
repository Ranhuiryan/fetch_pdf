import glob, os, shutil

ftype = '*.pdf'
src = './files/*/'
pdf_list = glob.glob(src+ftype)

for pdf in pdf_list:
    pdf_name = os.path.basename(pdf)
    shutil.move(pdf, pdf_name)