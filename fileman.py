import re
from consts import Identifiers
import json

class Config:

    def read():
        with open(Identifiers.config) as saved:
            config = saved.read()
            config = str(config).replace("let config = ", "")
            buf = re.sub(";(\\n|.)*", "", str(config))
            buf = re.sub("(\\S.+)(?=: )", "\"\\1\"", buf)
            buf = re.sub("(\\t*(\\n+| \\s+))\\t*", "", buf)
            out = json.loads(buf)
            return out
    


    
    def write(new_config):

        Config.write(new_config, Identifiers.config)
    
    def write(new_config, location):
        with open(location, "w") as saved:

            saved.write("let config = ")
            buf = json.dumps(new_config, sort_keys=True, indent=4)
            buf = re.sub("(\")(\\S.+)(\")(?=: )", "\\2", buf)
            # buf = re.sub("(.{1}$)", "", buf)
            saved.write(buf)
            saved.write("; \n\n")
            saved.write("if (typeof module !== \"undefined\") { module.exports = config; }")

        