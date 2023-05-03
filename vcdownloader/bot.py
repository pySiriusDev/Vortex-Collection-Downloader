from botcity.core import DesktopBot, Backend
from psutil import Process
from win32gui import FindWindow
from os import listdir
from pywinauto.findwindows import ElementNotFoundError


class Bot(DesktopBot):
    def action(self, execution=None):
        self.vortex_window_title: str = 'vortex'
        self.img_path: str = './assets'
        self.img_labels = list()

        self.load_images()
        self.run()

    @property
    def treshold(self) -> int:
        treshold = input('Max mods to download: ')
        try:
            return int(treshold)
        except ValueError:
            print('\nEnter numbers only!')
            return 0

    @property
    def hwnd(self) -> int:
        return FindWindow(None, self.vortex_window_title)

    def load_images(self) -> None:
        for image in listdir(self.img_path):
            label = image.split('.')[0]
            path = self.img_path + '/' + image
            self.add_image(label, path)
            self.img_labels.append(label)
        self.img_labels = sorted(self.img_labels, reverse=True)

    def health_check(self, task_number: int):
        if task_number > 9 and task_number % 10 == 0:
            process = self.find_process('chrome.exe')
            process = process if type(process) == Process else process[0]
            self.terminate_process(process)  # type: ignore
            self.wait(1000)

    def run(self) -> None:
        self.connect_to_app(backend=Backend.UIA, handle=self.hwnd)
        download_started = False
        window = self.find_app_window(handle=self.hwnd)
        for x in range(self.treshold):
            while not download_started:
                v_download = self.find_app_element(
                    from_parent_window=window, title='Download')
                if v_download is not None:
                    self.wait(1000)
                    try:
                        v_download.click()
                    except ElementNotFoundError:
                        print('')
                b_download = self.find(label='b_download')
                if b_download is not None:
                    self.wait(1000)
                    self.click_on('b_download')
                    download_started = True
            download_started = False
            self.health_check(x)
