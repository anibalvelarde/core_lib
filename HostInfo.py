
class HostInfo:
    import os

	def __init__(self, hostType):
        if hostType is None
            self.hostIp = "127.0.0.1"
            self.hostName = "localhost"
            self.hostType = "default"
            return
            
        if hostType == "DB"
            self.hostIp = os.environ['MES_DB_IP']
            self.hostName = "DatabaseHost"
            self.hostType = hostType
            return
            
        raise Exception('HostType {} is not supported'.format(hostType))