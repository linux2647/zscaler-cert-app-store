import logging
import os
import subprocess
import pdb

class UpdateCertStore(object):
    def __init__(self):
        # self.GetZscalerRoot()
        self.installed_apps = self.installed_apps()

    def installed_apps(self):
        """Method to identify installed apps """
        result = {}
        for app in ['python3', 'git', 'ruby']:
            print(app)
            resp = subprocess.run(f'{app} --version', shell=True, capture_output=True)
            if 'not found' in resp.stdout.decode('utf-8'):
                result[app] = {
                    'installed': False,
                    'version': None,
                    'zscertInstalled': False
                }
            else:
                result[app] = {
                    'installed': True,
                    'version': resp.stdout.decode('utf-8').strip(),
                    'zscertInstalled': False}

        print(result)
        return result

    def GetZscalerRoot(self):
        """Method to download Zscaler root Certificate from keychain and store it under ~/ca_certs"""
        path = os.path.expanduser("~")+'/ca_certs'
        if not os.path.exists(path):
            resp = subprocess.run('mkdir ~/ca_certs', shell=True, capture_output=True)
            print(resp)
        subprocess.run('security find-certificate -c zscaler -p >~/ca_certs/ZscalerRootCertificate.pem', shell=True,
                       capture_output=True)
        return

    def app_python(self):
        """Method to update python CA trusted store"""
        cmd = 'cat ~/ca_certs/ZscalerRootCertificate.pem >> $(python3 -m certifi)'
        resp = subprocess.run(cmd, shell=True, capture_output=True)
        print(resp)
        self.installed_apps['python3'].update(zscertInstalled=True)
        print(self.installed_apps)

    def app_git(self):
        """Method to update git ca trusted store"""
        cmd = 'git config --global http.sslcainfo ~/ca_certs/ZscalerRootCertificate.pem'
        resp = subprocess.run(cmd, shell=True, capture_output=True)
        print(resp)
        self.installed_apps['git'].update(zscertInstalled=True)

    def app_ruby(self):
        """
        Method to update ruby ca trusted store
        gem update --system  shows ERROR:  SSL verification error
        """
        cmd = 'gem cert --add ~/ca_certs/ZscalerRootCertificate.pem'
        resp = subprocess.run(cmd, shell=True, capture_output=True)
        self.installed_apps['ruby'].update(zscertInstalled=True)

    def app_curl(self):
        """
        Method to update golang ca trusted store
        curl recognizes the environment variable named 'CURL_CA_BUNDLE' if it is set, and uses the given path as a path
        to a CA cert bundle.
        gem update --system  shows ERROR:  SSL verification error
        """
        cmd = 'gem cert --add ~/ca_certs/ZscalerRootCertificate.pem'
        resp = subprocess.run(cmd, shell=True, capture_output=True)
        self.installed_apps['ruby'].update(zscertInstalled=True)