# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import requests
r = requests.get('https://github.com/timeline.json')
r.json()