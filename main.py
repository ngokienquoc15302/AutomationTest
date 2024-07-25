import pytest
import pdfkit
import os


def run_pytest_and_generate_report():
    html_report = 'reports/report.html'
    pytest.main(['--html=' + html_report, '--self-contained-html'])

    pdf_report = 'reports/report.pdf'
    convert_html_to_pdf(html_report, pdf_report)


def convert_html_to_pdf(html_file, pdf_file):
    try:
        pdfkit.from_file(html_file, pdf_file)
        print(f"Đã chuyển đổi thành công từ {html_file} sang {pdf_file}")
    except Exception as e:
        print(f"Lỗi trong quá trình chuyển đổi: {e}")


if __name__ == "__main__":
    if not os.path.exists('reports'):
        os.makedirs('reports')

    run_pytest_and_generate_report()
