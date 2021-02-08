from WebSelenium.ApiTestStudy.api.department import Department


class TestDepartment:
    department = Department()

    def test_department_list(self):
        r = self.department.list(1)
        assert self.department.jsonpath(expr="$..name")[0] == "WestWayyt"
