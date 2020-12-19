import docx2txt
import split
import glob

for file in glob.glob("*.docx"):
    file = file.replace('.docx','')
    for en_file in glob.glob("*_EN.docx"):
        english_file_name = en_file.replace('_EN.docx','')
        if file == english_file_name:
            print("Preparing: " + file)
            # read in word file
            message_title = file
            resultPT = docx2txt.process(file + ".docx")
            resultEN = docx2txt.process(file + "_EN.docx")

            data_to_print_pt = split.split_into_paragraphs(resultPT)
            data_to_print_en = split.split_into_paragraphs(resultEN)

            file1 = open(message_title+".tsv","w")

            i = 0
            for line in data_to_print_en:
                if i < len(data_to_print_pt):
                    file1.write(line + '\t' + data_to_print_pt[i] + '\n')
                    i += 1
                else:
                    file1.write(line)


            file1.close()

            print(len(data_to_print_pt))
            print(len(data_to_print_en))
        

