# -*- coding: utf-8 -*-
__title__ = "Hello\nWorld"
__doc__ = "환경 테스트용 버튼"

from pyrevit import revit, DB, script

doc = revit.doc
output = script.get_output()

walls = DB.FilteredElementCollector(doc)\
          .OfCategory(DB.BuiltInCategory.OST_Walls)\
          .WhereElementIsNotElementType().ToElements()

output.print_md("## 벽 개수: **{}**".format(len(walls)))
for w in list(walls)[:5]:
    print(output.linkify(w.Id), w.Name)
