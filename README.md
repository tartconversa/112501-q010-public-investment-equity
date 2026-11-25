# 教育医疗公共投入组合资料基线

CSV 使用 UTF-8 编码，首行为字段名。资料仅提供项目所需的合成事实，空值代表来源尚未提供。

- `projects.csv`：基线资料，首行为 `project,sector,township,stage,budget,approved_on`。
- `population.csv`：基线资料，首行为 `township,group,period,count_low,count_high,trend_version`。
- `capacity.csv`：基线资料，首行为 `facility,sector,township,period,capacity,used,source_version`。
- `outcomes.csv`：基线资料，首行为 `project,period,service_group,served,access_minutes,maintenance_need`。

## 基线检查

运行 `python3 -m unittest discover -s tests -v` 可检查资料可读性、主键唯一性和版本锚点。该检查不实现业务分析能力。
