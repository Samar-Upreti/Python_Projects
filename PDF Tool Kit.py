from pypdf import PdfReader, PdfWriter
import sys

# Core PDF Functions

def count_pages(pdf_name):
    reader = PdfReader(pdf_name)
    return len(reader.pages)


def merge_pdfs(pdf_files, output_name):
    writer = PdfWriter()

    for pdf in pdf_files:
        writer.append(pdf)

    writer.write(output_name)

    return output_name


def split_pdf(pdf_name, output1="PDF_1.pdf", output2="PDF_2.pdf"):
    reader = PdfReader(pdf_name)

    total_pages = len(reader.pages)
    midpoint = total_pages // 2

    writer1 = PdfWriter()
    writer2 = PdfWriter()

    for page in range(midpoint):
        writer1.add_page(reader.pages[page])

    for page in range(midpoint, total_pages):
        writer2.add_page(reader.pages[page])

    with open(output1, "wb") as f:
        writer1.write(f)

    with open(output2, "wb") as f:
        writer2.write(f)

    return output1, output2


def extract_text(pdf_name, output_file="PDF_Extracted.txt"):
    reader = PdfReader(pdf_name)

    with open(output_file, "w", encoding="utf-8") as f:

        for page in reader.pages:
            text = page.extract_text()

            if text:
                f.write(text)
                f.write("\n")

    return output_file


def view_metadata(pdf_name):
    reader = PdfReader(pdf_name)

    metadata = reader.metadata

    if metadata is None:
        return {}

    return {
        "Title": metadata.get("/Title"),
        "Author": metadata.get("/Author"),
        "Creator": metadata.get("/Creator"),
        "Producer": metadata.get("/Producer")
    }


# Menu

def menu():

    while True:

        print("\n===== PDF TOOLKIT =====")
        print("1. Merge PDFs")
        print("2. Split PDF")
        print("3. Count Pages")
        print("4. Extract Text")
        print("5. View Metadata")
        print("6. Exit")

        try:
            choice = int(input("Choose: "))

            match choice:

                case 1:
                    n = int(input("How many PDFs to merge: "))

                    pdfs = []

                    for i in range(n):
                        pdfs.append(
                            input(f"Enter PDF {i+1}: ")
                        )

                    output = input(
                        "Output file name (without .pdf): "
                    )

                    result = merge_pdfs(
                        pdfs,
                        f"{output}.pdf"
                    )

                    print(f"Merged Successfully -> {result}")

                case 2:
                    pdf_name = input("Enter PDF Name: ")

                    file1, file2 = split_pdf(pdf_name)

                    print("Split Successful")
                    print(file1)
                    print(file2)

                case 3:
                    pdf_name = input("Enter PDF Name: ")

                    pages = count_pages(pdf_name)

                    print(f"Total Pages: {pages}")

                case 4:
                    pdf_name = input("Enter PDF Name: ")

                    output = extract_text(pdf_name)

                    print(f"Text Extracted Successfully -> {output}")

                case 5:
                    pdf_name = input("Enter PDF Name: ")

                    metadata = view_metadata(pdf_name)

                    if not metadata:
                        print("No Metadata Found")

                    else:
                        print("\n===== PDF INFO =====")

                        for key, value in metadata.items():
                            print(f"{key}: {value}")

                case 6:
                    print("Thanks For Using PDF Toolkit :)")
                    sys.exit()

                case _:
                    print("Invalid Option")

        except FileNotFoundError:
            print("PDF Not Found!")

        except ValueError:
            print("Invalid Input!")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    menu()