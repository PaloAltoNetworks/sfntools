
# THIS IS NOT DONE AT ALL...
#
# NEEDS A LOT OF WORK AND WE MAY NOT NEED IT
import os.path
import random
import logging
import argparse


# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('dns-gen.log')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)


def generator(num_queries, domain_file):
    
    # First check to make sure we can read the file
    if not os.path.isfile(domain_file):
        logger.error("Unable to open the file {0} - exiting".format(domain_file))
        print("\nUnable to open the file {0}, please check filename and permissions\n".format(domain_file))
        exit(0)

    # Run through the loop for the given number of queries that we need
    for index in list(range(num_queries)):
        print(random.choice(list(open(domain_file))))
        srcIP = "192.168.55.{0}".format(random.randrange(200,240,2))
        print(srcIP)
        packet = (IP(src="192.168.55.200",dst="8.8.8.8")/UDP(sport=RandShort())/DNS(id=1000,rd=1,qd=DNSQR(qname="qixqnto.in")))













if __name__ == '__main__':
    
    
    logger.info("DNS Generator STARTING")

    # Parse arguments to set file to read domains from and number of queries
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", dest = "domain_file", 
                        help = "file of domain names to use : DEFAULT is bad_domains.txt",
                        metavar = "FILE", default = "bad_domains.txt" )
    parser.add_argument("-n", "--number", dest = "num_queries",
                        help = "number of DNS queries to generate : DEFAULT is 100",
                        default = 100)
    args = parser.parse_args()

    
    print("\nGenerating {0} random queries from file {1}".format(args.num_queries,args.domain_file))
    logger.info("Generating {0} random queries from file {1}".format(args.num_queries,args.domain_file))
    
    generator(int(args.num_queries),args.domain_file)
