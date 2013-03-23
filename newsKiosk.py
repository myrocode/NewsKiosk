__author__ = 'Miro Radenovic'

import config
import logging
import logging.handlers
from subprocess import Popen


cmd_convert_recipt_to_mobi = 'ebook-convert {from} {to}  --output-profile kindle'

cmd_send_mobi_to_kindle = 'calibre-smtp -r {server} --port {port} --username {username}'\
                          ' --password {password} {from} {to} {title} '\
                          '--attachment {mobi}'


def main():
    pass

def convert_recipe_tp_mobi(recipt):
    mobiFile= recipt.lower().replace('recipt','mobi')
    p = Popen('ebook-convert {recipePath} {tempFolder} --output-profile kindle'.format(
            recipePath=config.calibre_recipies_path + recipt, tempFolder=config.calibre_tmp_mobi_path + mobiFile))
    stdout, stderr = p.communicate()
    logging.info(stdout)


if __name__ == "__main__":
    root = logging.getLogger()
    root.setLevel('info')
    timedFileLogger = logging.handlers.TimedRotatingFileHandler('VMExplorer.log',when='h', backupCount=10)
    root.addHandler(timedFileLogger)
    main()