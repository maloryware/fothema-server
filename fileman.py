from os import close
import re
from consts import Identifiers
import json

class Config:

    def read(x):
        with open(Identifiers.config) as saved:
            config = saved.read()
            config = str(config).replace("let config = ", "")
            buf = re.sub(f";(\n|.)*", "", str(config))
            buf = re.sub(f"(\S.+)(?=: )", '"\1"', buf)
            buf = re.sub(f"(\t*(\n+| \s+))\t*", "", buf)    
            io = ["", "", "", ""]
            io[0] = buf[0:400]
            io[1] = buf[400:800]
            io[2] = buf[800:1200]
            io[3] = buf[1200:1600]
            return str(io[x])
            

    def saveToBuffer(new_config_section):
        with open(Identifiers.buf, "a") as buf:
            buf.write(new_config_section)
    
    def writeFromBuffer():
        with open(Identifiers.buf) as b:
            Config.write(b.read(), Identifiers.config)
    
    def write(new_config, location):
        with open(location, "w") as saved:

            saved.write("let config = ")
            buf = json.dumps(new_config, sort_keys=True, indent=4)
            buf = re.sub(f'(")(\S.+)(")(?=: )', f'\2', buf)
            saved.write(buf)
            saved.write("; \n\n")
            saved.write("if (typeof module !== \"undefined\") { module.exports = config; }")

        