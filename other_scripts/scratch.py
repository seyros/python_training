import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-22s %(levelname)-8s %(message)s', \
                                    datefmt='%m-%d %H:%M')

with open("/usr/lib/jenkins/111") as f:
        n=0
        for line in f.readlines():
                line=line.strip()
                if os.path.exists(line):
                        logging.info('current removed file:   {}'.format(line))
                        os.remove(line)
                        if os.path.exists(line):
                                logging.info('SUCCESS!!! file {} removed NOW!!!'.format(line))
                                n+=1
                        else:
                                logging.info('Unsuccessfull!!! file {} don\'t removed NOW!!!'.format(line))
                else:
                        logging.info('NOT FOUND file:   {}'.format(line))
logging.info('SUCCESSfully  removed {} files'.format(n))
