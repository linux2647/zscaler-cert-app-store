# zscaler-cert-app-store
Adds Zscaler root certificate into different application CA stores. Currently works only in OSX

# Installation 
```bash
git clone https://github.com/sergitopereira/zscaler-cert-app-store.git
pip3 install -r zscaler-cert-app-store/requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
```

# usage
```bash
python zscaler-cert-app-store -h
usage: zscaler-cert-app-store [-h] [-p] [-d] [-g] [-r] [-c] [-w] [-n] [-l] [-v]

optional arguments:
  -h, --help      show this help message and exit
  -a, --all       Add Zscaler root certificate to all installed applications
  -p, --python    Add Zscaler root certificate to pip and requests.Note that python2 is not supported
  -d, --download  Download Zscaler root certificate from keychain
  -g, --git       Add Zscaler root certificate to git
  -r, --ruby      Add Zscaler root certificate to Ruby
  -c, --curl      Add Zscaler root certificate to curl
  -w, --wget      Add Zscaler root certificate to wget
  -n, --npm       Add Zscaler root certificate to NPM
  -l, --libressl  Add Zscaler root certificate to libressl. This needs to be executed as root
  -v, --version   Script version
    
```
In order to install all applications that are installed run the following command
```bash
zscaler-cert-app-store -a
```


# Requirements
```bash
if Zscaler root certificate is not downloaded via script, please download to
~/.zscaler-cert-app-store/ZscalerRootCertificate.pem

python3
pip3
```
# Script  commands

Python3 : The script uses pip-system-certs package and will patch the PIP and requests in oder to 
use certificates from the default system store rather than the bundled certificates CA
```bash
  command: cat ~/.zscaler-cert-app-store/ZscalerRootCertificate.pem >> $(python -m certifi)
```
NOTE: Python 2 is not supported.

git: The script  will run the following command
```bash
  command: git config --global http.sslcainfo  ~/.zscaler-cert-app-store/ZscalerRootCertificate.pem/ZscalerRootCertificate.pem
```
curl: will add  CURL_CA_BUNDLE environment variable depending on the user terminal
```bash
  command: echo "export CURL_CA_BUNDLE=~/.zscaler-cert-app-store/ZscalerRootCertificate.pem" >> $HOME/.bashrc
  or
  command: echo "export CURL_CA_BUNDLE=~/.zscaler-cert-app-store/ZscalerRootCertificate.pem" >> $HOME/.zshrc
```
wget: will tun the following command
```bash
  command: echo "ca_certificate=~/.zscaler-cert-app-store/ZscalerRootCertificate.pem" >> $HOME/.wgetrc
```
Ruby: will add SSL_CERT_FILE environment variable depending on user bash
```bash
  command: echo "export SSL_CERT_FILE=~/.zscaler-cert-app-store/ZscalerRootCertificate.pem" >> $HOME/.bashrc
  or
  command: echo "export SSL_CERT_FILE=~/.zscaler-cert-app-store/ZscalerRootCertificate.pem" >> $HOME/.zshrc
```

# LibreSSL
This need to be executed as root!
```bash
cat /home/root/.zscaler-cert-app-store/ZscalerRootCertificate.pem >>/private/etc/ssl/cert.pem
```

For more information, refer to https://help.zscaler.com/zia/adding-custom-certificate-application-specific-trusted-store#edge-browser

