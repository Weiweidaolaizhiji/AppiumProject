import pytest
import yaml


class TestYaml:
    @pytest.mark.parametrize("name",("search","main"))
    def test_yaml_file(self,name):
        with open("../common/searchname.yaml",encoding="utf-8") as f:
            steps = yaml.safe_load(f)
            print(steps)
        for step in steps:
            if step == name:
                values = steps[name]
                print(values)
                for value in values:
                    print(value)
        #     element = None
        #     # if "by" in step.keys():
        #     #     element = self.find(step["by"],step["locator"])
        #     if "action" in step:
        #         action = step["action"]
        #         if "click" == action:
        #             self.find(step["by"],step["locator"]).click()
        #         if "send" == action:
        #             self.find(step["by"],step["locator"]).send_keys(step["value"])