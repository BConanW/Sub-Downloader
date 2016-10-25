# import time
# import sys
# import os
# #import pycurl
# import cStringIO
# import hashlib
# import argparse
# import json
# import datetime
# import urllib
# import multiprocessing
# import xml.etree.cElementTree
import logging
import time

class StdoutLogger:
    def __init__( self, level=1 ):
        self.__level = level
        timestr = time.strftime("%Y%m%d-%H%M%S")
        logname = "%s.log" % timestr
        logging.basicConfig(filename=logname, level=logging.DEBUG)

    def info( self, msg ):
        print('[INFO]', msg)
        logging.info(msg)
        
    def warn( self, msg ):
        logging.warning(msg)

    def error( self, msg ):
        logging.error(msg)
    # def info1( self, msg ):
    #     if self.__level >= 1:
    #         print('[info1]', msg)
    #
    # def info2( self, msg ):
    #     if self.__level >= 2:
    #         print('[info2]', msg)
    #
    # def info3( self, msg ):
    #     if self.__level >= 3:
    #         print('[info3]', msg)



#def main( argv ):
#    log = StdoutLogger()
#    test_data_root_dir = os.getcwd()
#    # parse the command line
#    progname = os.path.basename( argv[0] )
#    next_arg = 1
#
#    config_file = ''
#    while len(argv) > next_arg and argv[next_arg][0:2] == '--':
#        if len(argv) > (next_arg+1) and argv[next_arg] == '--config-file':
#            next_arg += 1
#            config_file = argv[next_arg]
#            next_arg += 1
#
#        elif len(argv) > (next_arg+1) and argv[next_arg] == '--log-file':
#            next_arg += 1
#            config_file = argv[next_arg]
#            next_arg += 1
#
#        else:
#            print '%s: Unknown switch %s' % (progname, argv[next_arg])
#            return 1
#
#    if len(argv) > next_arg:
#        print '%s: Unused arguments on command line %r' % (self.progname, argv[next_arg:])
#        return True, 1
#
#    config_data = _getDefaultConfigData()
#    
#    if os.path.exists( config_file ):
#        with open(config_file) as f:
#            config_data = f.read()
#
#    config = json.loads( config_data )
#
#    for channel_config in config['all_channels'] :
#        log.info( 'starting subscriber manager manager' )
#        subscriber_mgr_mgr = SubscriberManagerManager( log, test_data_root_dir, channel_config  )
#        subscriber_mgr_mgr.start()