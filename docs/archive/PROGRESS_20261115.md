# 破茧助手实验项目进度日志

> 项目目录：`D:\信息茧房`  
> 建立日期：2026-11-08  
> 本次记录核对截至：2026-11-15（北京时间，UTC+8），步骤44（经用户明确指令由 Antigravity 直接执行）已将 5 分钟答辩演示页升级为高定科学编辑部×精密光学沙盘 `five_minute_showcase_v3`（`showcase_5min.html` SHA-256 `461ad2a9…8c3d93`，双环认知核徽章、双弧光学透镜、跨轨共享证据桥、平行双轨曲线与四维胶囊哑铃图，彻底根治步骤43 `v2` 的梯形火柴人、硬黑框与斜线/虚线穿字碰撞），`verify_five_minute_showcase` 新增反硬块阴影、反简笔火柴人路径、光学渐变定义门禁，`test_showcase` 扩充至 22 项；纯离线 ¥0.00；最新全项目 **1053 项通过**（`validation_20261115T074220_086089.json`），受保护三件套与账本（772 行）字节不变。以下为步骤43 时的状态：步骤43已把此前未入档的 5 分钟演示页初稿（`five_minute_showcase_v1`）重构为无 Emoji 的一屏一图动态交互沙盘 `five_minute_showcase_v2`（`showcase_5min.html`，四幕定制 SVG 舞台覆盖视口约 79–82%，长文收进默认关闭的侧滑抽屉，提词器默认隐藏），`verify_five_minute_showcase` 新增 `_ui_sandbox_audit` 与 `_payload_truth_audit` 硬门禁，`test_showcase` 19 项；纯离线 ¥0.00；最新全项目 **1050 项通过**（`validation_20261115T051501_af533a.json`），受保护三件套与账本（772 行）字节不变。以下为步骤42 时的状态：步骤42已完成方案 §5.4 封闭虚构情境 TOPIC_SYNTH_01（星澜市，全部标 synthetic）真实 `mimo-v2.6-flash` 实证：5 次运行全部留痕（4 次失败/中断 + 1 次完成，136 次 HTTP，¥0.44355880），最终运行 55 次调用、16 测量 + 16 盲评、清单离线核验通过；T0 去先验成功（BS 0.25），T1 未出现预期茧房致盲，I5/I4 锚题全纠（BS 0.0025）且主终点并列；看板新增 7 步路演导览、提词卡与双轨对比专区；总结案报告与五人答辩攻略已交付；账本已结算累计 ¥1.58175440（2 条授权持有合计 ¥2.103296）；最新全项目 1031 项通过，步骤28–41 原件字节不变，真人审核仍0。
> 用途：保存已做的事情、实际结果、产物、失败、费用与下一步，供继续工作时接续。不是实验效果报告，也不替代原始日志。

## 1. 当前停在哪里

**步骤38修复用户实机发现的看板排版缺陷：旧 `.chip` 未声明盒模型、默认 `display:inline`，其内嵌 `display:block` 的 `<small>` 触发浏览器行内盒拆裂，导致时间轴胶囊边框从中间断开并逐行竖排；`renderTimeline()` 又把胶囊直接拼进 `<p>` 而未用 `.chips` 弹性容器。**现将 `.chip` 改为 `display:inline-flex;flex-direction:column`（`border-radius:10px`），静态 `view-02` 与动态 `live-02` 统一为 `.timeline`→`.timeline-row`（158px＋1fr 两列）＋`.timeline-head`＋`.chips` 结构，同一区组 23 个阶段胶囊横向流式排列、窄屏自动折行；同时巡检全部11视图：`.table-wrap{overflow-x:auto}` 保护所有宽表（Python `_table` 与 JS `tblWrap` 双路径）、`.net-grid` 六张拓扑卡 3×2 网格（并移除动态区重复绘制的 SVG）、`.banner` 与 `.filters` 合并进单一 sticky `.topbar` 并删除 `top:56px` 偏移，消除横幅折行遮挡。实测 1440/900/430px 三断点胶囊越界数均为0、`scrollWidth==clientWidth`、6 个拓扑卡正常并排。`verify_dashboard_bundle` 新增 `_ui_layout_audit` 九项硬断言（胶囊盒模型、时间轴容器、表格滚动、网格、单一 sticky 顶栏、全页行内块冲突扫描）；`dashboard_data.json` 重建后与步骤37 逐键比对仅 `generated_at_utc` 与 `overview.milestones`（验证报告滚动窗口）两处差异，`panel`/`effects`/`trace_paths` 等24个顶层键逐字节相同（`dataset_sha256` 由 `c28bf300…3c3c9f` 变为 `af49d724…c769f`），证明仅改表现层、未动任何派生数值。**


**步骤39对剩余五轮发起真实 `mimo-v2.6-flash` 调用并完成 6/6 配对：`TOPIC_01_R2` 166、`TOPIC_02_R1` 223、`TOPIC_02_R2` 188、`TOPIC_03_R1` 176、`TOPIC_03_R2` 207 字符，全部落入各轮 `feasible_organized_ranges`（[141,214]/[145,257]/[141,238]/[132,205]/[140,227]），可见总长 619–764，I4/I5 最大相对差 2.377%，七项配对检查（同证据块、同来源映射、600–800、总长≤10%、附加段≤10%、同回应提示、装配可重建）逐轮全通过；`TOPIC_01_R2` 旧的 232 字符编辑稿偏差已由真实 166 字符输出取代。**新增 11 次真实调用、输入 23 922 tok / 输出 2 701 tok、六轮最终运行合计 ¥0.01765808；加连通性冒烟与被替代/中断尝试，本步实际支出 ¥0.02157376，账本累计 ¥0.03430324 → ¥0.05587700，剩余 ¥4.94412300，全部 settle 条目可加总核对。**必须披露：R1 复用运行有父级内部报告、其余五轮为纯证据包（`prompt_variant` 逐轮标注，非完全同条件）；3 处 I5 与中性臂文本重合（T01/R1↔I0、T02/R2↔I2、T03/R1↔I2）已登记 `dose_arm_collisions` 未规避；一次主控中断的真实尝试（¥0.002141）保留在 `live_deliveries/_aborted/`；仍 `subject_delivered=false`、`human_reviews_completed=0`、`full_I4_eligible=false`、`formal_eligible=false`。


**步骤40完成 TOPIC_01 真实端到端微型实证（`TOPIC_01/B02` 环境 D，S01=+1/S05=−1 × I0/I5/I4）：最终运行 `live_micro_pilot_TOPIC_01_20261113T071307Z_fce65143` 共 52 次真实调用、0 次被拒、¥0.18835572，16 份测量与 16 份盲评全部回填，离线重放核验通过（6 分支处理前哈希与父 T1 快照一致）。**主要发现是天花板效应：两名受试 T0 零曝光即锚题全对（Acc=100、S=0、U=100、BS 0.0072），曝光后 BS 降到 0.0034，三臂 T3 BS 均在 0.0025–0.0044，无可区分臂效应；n=2 机制演示，不作推断。**必须披露：前 3 次运行失败/中断（T1 发言超长、外层 600 秒超时、T1 测量输出发言而非 JSON），费用 ¥0.24038164 全部计入；一条在途请求登记 `uncertain/interrupted` 并按最坏情况 ¥1.050624 持有；经用户授权在 `budget.py` 新增单一 ID 白名单 `HELD_INTERRUPTED_REQUEST_IDS`，仅该请求不再阻塞新预留；最终运行前提示词做过两次格式/字数修订（v3）；S01 的 I0/I5 R1 回应逐字相同（R1 刺激相同 + temperature=0）。


**步骤41：共享账本经新增的 `raise_limit` 事件受控提额至 ¥50.00（原 257 行字节保留、可重放），并把 TOPIC_01（步骤40 复用，清单字节不变）、TOPIC_02（能源转型）、TOPIC_03（天气信息核查）合龙为三议题真实端到端实证矩阵：18 条反事实分支、采纳 156 次调用（实际 162 次，另 6 次为被拒重试与四阶段重做）、48 份真实测量 + 48 份真实盲评、6 份 mirror、36 段干预回应，三份清单与矩阵全部离线重放核验通过。**三议题一致呈天花板效应：6 名受试 T0 即锚题全对（Acc=100、S=0），三臂 T3 BS 均在 0.0025–0.0039，无可区分臂效应；可描述变化只在分叉前曝光阶段（TOPIC_03 BS 0.0216→0.0030、U 58→92）。**必须披露：B02 区组 TOPIC_02/03 的 S01/S05 同立场，经用户选定改用“S01 + 从 S05 起首个对立者”（TOPIC_02/03 均为 S07）；任务书议题名有误，以冻结证据包为准（能源转型/天气信息核查）；TOPIC_02 首次运行在 mirror 失败（¥0.07247108，已留痕），随后新增 mirror 逐条引句诊断反馈（`FEEDBACK_REVISION` v4，主提示词与校验器不变）后重跑完成。

**步骤42按方案 §5.4“封闭情境示例”构建全合成的 TOPIC_SYNTH_01 星澜市（甲方案双轨快速公交 / 乙方案氢能智轨），并完成真实端到端实证：最终运行 `closed_world_synth01_20261114T052738Z_8ac5d3e9` 共 55 次调用（3 次被拒重试），16 份测量与 16 份盲评全部回填，清单 `f2a3786d…20c2` 离线核验通过。**结果：T0 12 题全为 0.50（BS 0.2500，去先验成功）；8 轮同质 + 误导曝光后 T1 仍全为 0.50（**未出现预期的茧房致盲**，S01 发言转述网传数字，但测量以“无官方核查”保持不确定）；I5 与 I4 在 T2/T3 锚题全对（BS 0.0025）并经误导回流保持，I0 不变；**主终点 I4 与 I5 并列**；探索性指标 I4 迁移 4/4 对 I5 3/4、U 100 对 91.7、O 58.3 对 33.3。**必须披露：**①§5.4 表中“知识过强”行是“实体替换半合成”，本步采用表下封闭示例，已对表登记；②前 4 次运行失败/中断（组织段超窗、四阶段 blindspot 复述契约、上游 HTTP 500、组织段 JSON 未闭合），费用 ¥0.27526704 全部并入；③组织段提示 v1→v3 只改格式/长度；最终运行复用首跑已校验的四阶段输出（来源链与 blob 重验）；④经用户授权，HTTP 500 请求加入单 ID 持有白名单；⑤未在看到结果后修改封闭规则追求致盲。

**步骤43把工作区中未走标准流程、未入档的 5 分钟演示页初稿（`cocoon/showcase.py` 契约 `five_minute_showcase_v1` + 10 项未入回归的测试 + `showcase_5min.html`）正式接管并重构为 `five_minute_showcase_v2`：一屏一图的动态交互实验沙盘。**四幕主画面是由 Python 按真实数据确定性生成的 SVG 舞台：①克隆平行沙盘（培养皿 + 维恩 64/32/重叠 11 + 父快照克隆门 + 三舱 + 公平性天平，最大长度差 2.6%）；②茧房染色现场（48 信标逐列点亮、发帖原话气泡、答卷仪表 12/12 题 0.50、认知镜立场刻度与靶点）；③三条平行轨道（父快照哈希、I0/I5/I4 输入与信号、回应原话气泡 ≤24 字、T3 环与迁移格）；④双轨终局（先验天花板 vs 封闭新题曲线、四行点阵，O 指标红框标注“I5 33.3 优于 I4 58.3”、账本防伪条）。实测舞台覆盖视口 79–82%，桌面无页面滚动；长文全部收进默认关闭的四 Tab 侧滑抽屉；提词器默认隐藏、按 T 呼出；零 Emoji、零渐变字、零外链。`verify_five_minute_showcase` 新增 `_ui_sandbox_audit`（Emoji、渐变、提词器/抽屉默认关闭、四幕沙盘、主屏汉字 ≤45）与 `_payload_truth_audit`（原文、字数、七项检查、父哈希、主终点并列、迁移、O、Q5 错位披露）。**必须披露：**任务书写的“差值 ≤2.4%”与实测不符（最大 2.6%），页面按实测；任务书举例的短词气泡不是原话子串，页面只用逐字子串；本步费用 ¥0.00。

**步骤44（经用户明确指令“这次你直接写代码，不用给 Codex”，由 Antigravity 直接执行）针对步骤43 `v2` 截图复核发现的梯形火柴人、粗黑边框、`3px 3px 0` 硬阴影、第 2 幕认知镜斜线穿过“可确认性偏差”、第 3 幕虚线劈穿“709 字”、第 4 幕双线叠画混色等问题，将 `cocoon/showcase.py` 与 `showcase_5min.html` 全面重绘升级为 `five_minute_showcase_v3`（高定科学编辑部 × 精密光学仪器风）。**全页采用暖象牙白宣纸底 `#F8F6F1` 叠微米点阵、圆角悬浮卡片配 `<feDropShadow>` 柔光弥散投影、宋体衬线大标题与等宽数字对齐；重绘双环认知核徽章、双弧凸透镜、水平三次贝塞尔光纤诊断卡、四列流式平行泳道与跨轨共享证据桥、平行微偏移双轨曲线及四维胶囊哑铃图。Playwright `1440×900` 十状态截图逐帧核验零文字碰撞、零滚动溢出、零运行期报错；`_ui_sandbox_audit` 新增反硬块阴影、反简笔火柴人路径、光学渐变定义三项硬门禁，`tests/test_showcase.py` 扩充至 22 项，全项目 **1053 项通过**（`validation_20261115T074220_086089.json`），费用 ¥0.00，受保护原件 100% 未变。

| 工作项 | 当前状态 | 已核实的结果 |
|---|---|---|
| 原实验方案 | 已恢复并登记 | 根目录文件与原记录哈希一致 |
| 调度、指标、运行时与审计框架 | 已实现并离线验证 | 不是OASIS真实网络或完整实验结果 |
| 原助手与提示词 | 已冻结、已适配 | 不执行原网页；无模拟回退；原件保留 |
| MiMo连通性 | 真实通过 | 1次调用，返回连接成功 |
| 三议题候选证据 | 已制作 | 18条释义、13个来源页面、9份JSON包（含两轮切分草案） |
| 双人人工审核 | 未完成 | 完成人数为0；AI审核不计作人审 |
| 等证据剂量编辑稿 | 已通过结构与字数检查 | 6对、12份消息，690–796字符；不是实际完整I4 |
| 真实四阶段助手 | 流程与结构通过，语义待修 | 4次调用；39项输出中AI标出11项问题 |
| 独立短投递v1 | 失败历史保留 | 首段403字符超限，未调用第二段 |
| 独立短投递v2 | 失败历史保留 | 组织侧630通过；普通侧字段类型与句长失败 |
| 独立短投递v3 | 双模型配对仍失败 | 两侧版本类型已正确；组织侧632通过，普通侧附加155<160未接纳 |
| 整句摘录式对照备选 | **结构与剂量匹配，仅探索性候选** | 真实组织侧632＋确定性原句对照637；新增模型调用0，不重标v3成功 |
| 六轮离线可行性 | 已完成限定范围 | 41句、72组合；六轮有条件可行，仅1轮有既有真实组织侧 |
| 双人审核模板 | 已整理，尚未填写 | 55项、110个人工审核位；身份、时间、意见均空或pending |
| 独立AI语境审阅 | 已保存，仍需人审 | 41句语境检查、6项人审优先关注；非语义批准，不改写原JSON |
| 跨轮静态审阅交付 | 步骤28历史交付保留 | 页面与清单仍附当时644项回归，不覆盖旧文件 |
| 双人审核合并与裁决核验 | 步骤29历史实现保留 | 39项工作流测试仍通过，未处理真实已签副本 |
| 测量、私有评分与盲评契约 | 步骤30行为保持 | 原40项兼容测试通过，8/4分母分开、未生成正式金标准 |
| T1测量自报桥接 | 原备选保留 | subject_measurement_extracted，仍非方案常规发言 |
| T1常规发言桥接 | 步骤31实现 | subject_routine_speech，来源契约对齐；不认证实际生成 |
| 匿名registry与盲评回填 | 步骤31实现 | 确定性中性ID、私有条件映射/可信摘要及个体长面板；全部测量66项测试通过 |
| 网络级聚合与缺失敏感性 | 步骤32实现 | 8人以上网络缺测时精确均值为None；BS上下界按固定期望人数分母，8锚/4迁移隔离 |
| 2×2曝光与干预配对分析 | 步骤32实现 | 直接调用metrics.exposure_contrasts与paired_summary；主/次比较分开，T1共享校验 |
| 基于实际槽位的随机化检验 | 步骤32实现 | 仅提供经scheduling.allocate重建的allocations才计算p_raw/Holm p_adjusted；否则全为None |
| TOPIC_01三区材料包 | 步骤33实现 | 4真源/6证据绑定、108张卡180–220字符、96次四环境排程100%可解、12份600–800干预包 |
| 公共问卷与私有金标准 | 步骤33实现 | 8锚题4真4假＋4迁移题与6维量规，100%通过measurement两个严格校验器 |
| §5.2双人核验模拟演练 | 步骤33实现，步骤34推广三议题 | 八步全覆盖、分歧拦截→独立第三人裁决闭环；仅结构演练，真人签字仍0 |
| 三议题并行标准化引擎 | 步骤34实现 | 统一pilot_manifest、build_id与protocol_sha256；三议题各96次排程/12剂量包全可解 |
| 统一门限校验 | 步骤34实现 | 锚题8题绑定6维、12包全绑定摘录对照、每个真源权利预警完整传递 |
| 三议题全链路离线系统预演 | 步骤35实现 | `cocoon/system_rehearsal.py` 四阶段合龙：24曝光世界、36六臂分支、1248样本全量回填、156网络记录 |
| 六臂全量合规可见文本 | 步骤35实现 | `I0–I5` 两轮576次投递均为600–800字符，补齐旧 `dry_run` 的 `I0–I3` 空文本缺口，旧行为未改 |
| T1常规发言→mirror | 步骤35实现 | 192次严格契约重放，冻结证据包按字节哈希只读加载，user_quote 为 user_view 原文子串 |
| 网络级2×2与槽位随机化 | 步骤35实现 | T2/T3两个终点均输出 `p_raw` 与 `metrics.holm` 校正 `p_adjusted`；全部数值仅为合成演练 |
| 方案A双视角独立核验 | 步骤36实现 | 55项两列共110槽位自动生成，单列越权0，第三人裁决4项真实分歧 |
| 方案A权威合并核验 | 步骤36实现 | 直接走步骤29两个API：110槽/55项/0未决/2角色列/内容与7门禁全通过 |
| 方案A受控放行门禁 | 步骤36实现 | 默认锁定；`allow_ai_assisted_release=True` 才解锁 Pilot 放行，诚实保留真人未审与正式资格未授予 |
| 三议题全链路可视化看板 | 步骤37实现 | 单文件 `dashboard.html`：11视图、6筛选器、零外部CDN、响应式与打印样式 |
| 看板派生数据包 | 步骤37实现 | 1248面板样本、156网络记录、480轨迹、25条全链追溯；逐样本哈希与U三分项对账 |
| §12.4可视化验收 | 步骤37实现 | 25条路径/130节点重放、网络均值与2×2/Holm重算、方案A重跑一致、无外链无凭据 |
| 看板UI缺陷修复 | 步骤38实现 | `.chip` 改 `inline-flex` 列向，根治行内块撕裂；静态与动态时间轴统一 `.timeline-row`+`.chips` |
| 全视图排版与响应式 | 步骤38实现 | `.table-wrap` 横向滚动、`.net-grid` 3×2 网格、单一 sticky `.topbar`、无行内块嵌套冲突 |
| UI/DOM 防回归 | 步骤38实现 | `verify_dashboard_bundle` 新增9项 `ui_*` 断言；专项测试新增9项篡改与结构校验 |
| 六轮真实组织侧生成 | 步骤39实现 | 5 轮新调用（+R1 复用）全通过 `delivery.render_addition` 四句契约，落在各轮可行区间 |
| 六轮 I4/I5 结构配对 | 步骤39实现 | 6/6、七项检查全通过，可见总长 619–764，最大相对差 2.377% |
| 真实调用记账 | 步骤39实现 | 账本 23→59 行，本步 ¥0.02157376，累计 ¥0.05587700，`reconciled=true` |
| 材料包与看板接入 | 步骤39实现 | I4 改为真实输出、I5 确定性摘录；view-01/06/11 展示 6/6 状态、Run ID、Token 与费用 |
| 真实端到端微型实证 | 步骤40实现 | TOPIC_01/B02 环境 D，2 受试 × 3 臂，16 测量 + 16 盲评，52 次调用，离线重放核验通过 |
| 微型实证主要发现 | 步骤40实测 | 天花板效应：T0 即 Acc=100/S=0/U=100，三臂 T3 BS 0.0025–0.0044，无判别力 |
| 中断预留持有 | 步骤40授权变更 | `budget.HELD_INTERRUPTED_REQUEST_IDS` 仅 1 个 ID；其余未决原因照旧阻塞 |
| 看板真实实证专区 | 步骤40实现 | view-01/05/07/10 展示真实指标、发言、mirror、回应与节点追溯；verify 新增 9b 重验 |
| 账本受控提额 | 步骤41实现 | `raise_limit` 事件只升不降、可重放；共享账本 ¥5.00→¥50.00（seq 258） |
| 三议题真实实证矩阵 | 步骤41实现 | 18 分支、采纳 156/实际 162 次调用、48 测量+48 盲评；三清单与矩阵离线重放通过 |
| 三议题主要发现 | 步骤41实测 | 三议题均天花板效应，三臂 T3 BS 0.0025–0.0039 无判别力；变化只在曝光阶段 |
| 看板三议题矩阵专区 | 步骤41实现 | view-01/05/07/10 矩阵 KPI、3 张 SVG 轨迹、TOPIC_02/03 原文与追溯；verify 新增 9c |
| §5.4 封闭情境材料 | 步骤42实现 | `closed_world_pilot.py`：星澜市 6 条核查证据、8 锚 + 4 迁移、44 张论坛卡（12 张误导卡覆盖 5 道锚题）、I0/I4/I5，`is_synthetic_closed_world=True` |
| 封闭情境真实实证 | 步骤42实测 | 最终运行 55 次调用，16+16 回填；T0/T1 BS 0.25（未致盲），I5=I4 T2/T3 BS 0.0025，I0 不变；主终点 I4 与 I5 并列 |
| HTTP 500 持有 | 步骤42授权变更 | `budget.HELD_HTTP_ERROR_REQUEST_IDS` 仅 1 个 ID（uncertain+http_error），按最坏情况 ¥1.052672 持有 |
| 答辩路演看板 | 步骤42实现 | 7 步聚光灯导览 + 提词卡 + 双轨对比（5 指标双格 SVG）+ 合成情境原文；verify 新增 9d/9e |
| 5 分钟演示沙盘 | 步骤43实现，步骤44升级 v3 | `showcase.py` 契约 `five_minute_showcase_v3`；`showcase_5min.html` SHA-256 `461ad2a9…8c3d93`，逐字节可重现；`test_showcase` 22 项；讲稿 `FIVE_MINUTE_SHOWCASE_SCRIPT_20261115.md` |
| 结题文档 | 步骤42交付 | `FINAL_PROJECT_REPORT_20261114.md` 与 `DEFENSE_PRESENTATION_GUIDE_20261114.md` |
| 议题库规模 | 3个议题 | 真源4/5/4个、证据各6条；配额一致但真源数量按实际保留 |
| 冻结输入末次检查 | 已修复并测试 | 发送前、保存响应后、终态前检查父运行、packet、manifest、policy和来源表 |
| 正式I4/I5、受试Agent与OASIS | 未完成 | 没有真实T1自然观点、个性化镜像或正式干预结果 |
| 当前人工批准的正式材料 | 0 | 不把候选、适配测试或AI审核升级为正式批准 |

### 当前接续点：三议题标准化材料包与并行模拟审核已就绪，真人签字仍未执行

- 步骤32新建 `cocoon/analysis.py` 3个公共API：aggregate_panel_to_networks、analyze_exposure_2x2、analyze_intervention_effects；不改metrics/runtime/scheduling/measurement等旧模块。
- 由步骤31的 `reconciled_blind_panel_v1` 严格聚合到网络；缺测不静默剔除，精确均值置None并保留固定分母BS上下界；8锚题主终点与4迁移题探索终点分开。
- 2×2曝光效应直接调用 `metrics.exposure_contrasts`；干预效应统一归一化损失后调用 `metrics.paired_summary`，主确认性比较与4项次要探索比较分开标注。
- 只有提供经 `scheduling.allocate` 重建且与实际网络记录一致的allocations时，才用局部随机流在每个完整有效区组内重排六臂标签，按Phipson-Smyth保守口径算 `p_raw` 并调用 `metrics.holm` 得 `p_adjusted`；无allocations时p值全部为None，不以sign-flip冒充。
- 22项专项测试含从 `reconcile_blind_evaluations` 到曝光2×2的真实格式端到端闭环，全部为合成内存夹具，无新模型调用或费用。
- 步骤33以四个已取证真源构建TOPIC_01三区隔离Pilot候选材料包：区域1受试公共库+排程主表、区域2助手无标签证据包、区域3评估器私有金标准；`verify_topic01_pilot_materials`独立重验三区零泄漏、字数、排程、剂量与问卷哈希绑定。
- §5.2八步模拟演练输出恒定 `review_mode=simulated_rehearsal_not_human`、`human_reviews_completed=0`、`approved_for_experiment=False`、`formal_eligible=False`；`SIM_*`核验槽不是真人，`cross_topic_20261108/human_review_checklist.json`保持原空白状态且字节未变。
- R2编辑组织稿232字符超出整句摘录可行区间141–214，已作为 `deviation` 如实登记，不截断、不补字、不放宽10%阈值。
- 步骤34把上述逻辑参数化为三议题统一引擎：`build_all_topics_pilot_materials` 并行构建三议题并输出统一 `pilot_manifest`（含各议题 `build_id`、`protocol_sha256`），`verify_topic_pilot_materials(bundle, topic_id)` 用统一门限校验，`simulate_all_topics_dual_review` 并行汇总三议题分歧/裁决计数（默认3/3/3），诚实门禁在三议题上全部强制生效。
- 三议题真源数按实际保留为4/5/4，卡片配额、排程96次、讨论槽12、剂量12份、锚题8题4真4假＋4迁移题与6维细则完全一致；每个真源的 `redistribution_cleared=false` 与 `license_note` 完整传递，能源9条/天气2条历史取证排除记录保留。
- 后续需真人各自另存副本填写并走步骤29的核验API；在此之前任何材料、剂量或裁决结果都不得解释为已批准或已送达。

### 保留背景：测量契约与正式观测仍分离

- 新模块 `cocoon/measurement.py` 和40项内存测试完成，API/数据形状详见 `experiment/review/measurement_20261108/REPORT_step30_20261108.md`。没有发出问卷请求、盲评请求或生成现实议题真值。
- 实际原方案没有§8.5（第8节只有8.1/8.2）；本轮依据§5.3、第8节正文、§10和附录B实现隔离，不改原方案。
- 原方案要求T1自然观点来自常规发言；本轮指令要求从测量输出桥接。因此接口保留指定名但标记subject_measurement_extracted/natural_routine_speech=False/requires_protocol_review=True，不默认作为正式自然观点使用。
- 上层须提供明确的exposure_history已送达记录及T0/T1/T2/T3，prepared_inputs不进入可见ID白名单；真实性由上层事件验证，模块不认证实际送达。
- 实际人审/真实测量仍未执行，正式实验关闭，下一步等待用户转达新的接续指令。

### 保留背景：待真实独立副本提交

- 步骤29实现 `merge_and_verify_human_reviews` 与 `verify_human_review_submission`，API细节见 `REPORT_step29_20261108.md`。仅返回内存结果，不保存、不签署，真实人审计数仍0。
- 已填写副本仍须由真实审核者各自另存；当前未收到真实副本。第三人处理check分歧时须附完整bool的裁决checks，仅决定不同且check一致时可沿用一致值。
- 姓名/ID字符串核验不是身份认证，`identity_verified=False`；即使55项全部通过，full_108_card_review=False仍禁止正式放行。
- 最新683项测试通过。首次全回归4项旧文件写入错误及其诊断记录保留，未改权限、未删失败记录。

### 保留背景：跨轮离线审阅交付

- 输入 `experiment/review/cross_topic_20261108/` 内的 `feasibility.json`、`human_review_checklist.json`、`independent_review.json` 均冻结保留，不改写。
- `render_cross_topic_review` 兼容独立意见的顶层双哈希和 `input_sha256` 嵌套双哈希；若同时声明则全部必须与实际字节一致，不以另一种正确格式掩盖冲突。
- 独立意见为 `pass_with_context_review_required`：未发现限定范围的结构不一致，但6项语境重点仍待真人判断。两名真人独立审核与第三人分歧裁决尚未执行。
- 本轮不发起模型或API请求，不追加费用。后续按用户转达的Gemini指令执行，每轮独立生成Markdown汇报，并保留本日志。

### 保留的接续背景：v3与独立摘录备选

- v3运行 `delivery_20261108T105552Z_7fe7dae9d342459885c811b169a74ff1`，一次双阶段尝试2次HTTP，版本字段类型问题已解决；普通侧155低于160–192，配对仍失败。
- 没有再收费抽样。新建独立探索性整句摘录对照：组织侧真实原文175、完整632；普通侧选原证据整句180、完整637；附加段差2.86%，总长差0.79%，共同证据和回应提示一致。
- 新备选不是原v3模型配对的修复，普通侧明确非模型生成，组织4句/普通3句差异已披露。原v3失败、父长报告及原证据保持原样。
- 新备选位于 `experiment/review/delivery_v3_20261108/extractive_alternative.json`；通过限定范围AI复核，人工仍0，无实际T1/完整镜像、未发给受试Agent。
- 当前累计¥0.03430324，剩¥4.96569676；后续应确认是否采用该探索性普通阅读实现，而不是继续尝试靠提示词精确补字。

### 历史失败：短投递v2

- 运行ID：`delivery_20261108T101439Z_99cfd0db64294c3a8c51b1248b03eb98`；18:14执行2次调用，无自动重试。
- 组织反思侧：附加173字符、完整630字符，结构通过。
- 普通复述侧：JSON版本字段返回数字1.0而非字符串"1.0"，首错`invalid_schema`；仅事后诊断附加157字符，低于要求158–190，前三句也低于32字符槽位下限。
- 当前提示中“schema_version等于1.0”未明确字符串类型，是提示表达缺口；不因此静默修复原响应或推定模型故意违约。
- 两侧总长度看似630/614均在600–800内，但不代表配对合格：普通侧结构失败，附加段相对差约10.19%，超过10%。614仅诊断，未生成实际受试payload。
- 独立AI逐8句复核：7句支持、1句合理问题，没有发现新增事实问题；不能用AI语义通过豁免结构或长度失败，人审仍0。
- 本轮¥0.004389，累计¥0.029908，剩余¥4.970092；原报告与冻结输入未变，13事件/27blob核验通过。
- 当前尚无合格完整配对，无T1观点、无个性化镜像；下一步需新版本明确字段类型及改进句长生成。v1/v2都保留，不在本轮再次收费尝试。

### 历史失败：短投递v1

- 时间：2026-11-08 17:05:23–17:05:34。
- 运行ID：`delivery_20261108T090523Z_fb38842073a64ca4ae95b42c082d6f7e`。
- 终态：`delivery_failed`；失败阶段：`delivery_organized`。
- 错误：`length_out_of_range`，实际附加段 **403字符**，请求区间 **225–245字符**。
- 本轮固定证据、标题和公共回应提示共 **457字符**；由此推算完整消息为 **860字符**，仍超过原方案800目标。860是离线诊断，不是实际已送达受试Agent的消息。
- 请求区间225–245是本次生成策略，**不是原方案的额外硬标准**。原方案最终600–800在这个证据块下允许附加段143–343字符。
- 实际HTTP调用 **1次**；输入 **2,283 tokens**，输出 **338 tokens**，合计 **2,621 tokens**。
- 第二段 `plain_restatement` **未调用**；没有成功的I4/I5成对投递产物。
- 原长报告 **未修改**；失败的原始响应与调用记录均保留；没有裁剪、补字或自动重试。
- 已重新核验：**7项事件、17个blob，哈希链有效**。
- 结果文件：[历史v1短投递summary](experiment/delivery_probes/delivery_20261108T090523Z_fb38842073a64ca4ae95b42c082d6f7e/summary.json)。

## 2. 用户已确认的执行依据

1. 按根目录的[《破茧助手全量实验方案_v1.md》](破茧助手全量实验方案_v1.md)执行，不改为临时提出的教育主题。
2. 保留助手内部完整长报告，另生成最终投递文本；**不截断内部报告来假装达标**。
3. 第7.2节写的是受试Agent每轮可见材料**目标600–800中文字符**、两轮合计1200–1600。工程上暂以此作检查门槛，包含实际消息中的标签、标点、引用和空白，不是小米API上限。
4. I4/I5使用相同的新增证据片段和来源；总长及附加段长度分别检查，默认相对差不超过10%，公式为 `abs(I4-I5)/min(I4,I5)`。
5. 已确认小米普通按量API，模型 `mimo-v2.6-flash`，**首次小规模测试累计预算¥5**。该授权不等于受试预实验或全量实验预算。
6. 不以演示数据替代失败；不为挑选更好结果重复抽样；任何新提示词、显示或投递规则须留版本，保留旧运行。
7. 缺少T1自然观点时，不编造个体观点、不冒充镜像结果。人工审核未完成时不填“已通过”。
8. 本文件只记录凭据变量名 `MIMO_API_KEY`，**不记录密钥值、认证头或含密钥的执行命令**。此前凭据曾出现在聊天，应在控制台轮换；本日志不会复制它。

原方案SHA256：
`3d3ba6f0e21237cb288fe4a9558ab015a09b56f1a9538af81e5c9075637f6253`

## 3. 逐步工作记录

以下是根据现有会话、项目文件和执行记录补录的历史。没有可靠精确时间的步骤只写日期或阶段，不补造时间。后续在本节末尾追加，不把失败历史改成成功。

### 步骤01｜2026-11-07：确认实验边界与工程入口

- 核对原方案与目录约束，建立工程准备、正式运行及演示结果之间的边界。
- 配置包括3议题、6个seed区组、每世界16个Agent、4种曝光环境、6个干预臂及各轮次。
- 正式入口保持关闭；模型参数、预算、材料审核、平台接入等分项检查，不能仅改一个布尔值启动正式实验。
- 主要位置：`configs/core.json`、`cocoon/configuration.py`、`cocoon/__main__.py`、`cocoon/engineering.py`。
- 对应任务：1–5。

### 步骤02｜2026-11-07：实现调度与隔离数据接入入口

- 实现标准库调度接口，编写单元测试。
- 编写限制单条索引的AVeriTeC隔离接入脚本，候选标签与助手可见输入分开。
- 主要位置：`cocoon/scheduling.py`、`tests/test_scheduling.py`、`scripts/intake_averitec.py`。
- 对应任务：7–9。

### 步骤03｜2026-11-07：AVeriTeC获取失败，保留阻塞

- 指定版本的dev数据获取失败；状态为 `acquisition_failed`，返回 `URLError`，有效数据0字节、候选0条。
- 没有把失败下载说成已完成接入，没有把该候选当正式材料。
- 记录：[intake_status.json](experiment/review/intake_status.json)。
- 任务6、10仍受任务13阻塞；没有依据后续其他网站访问成功而擅自认定这一下载授权已恢复。

### 步骤04｜2026-11-07：实现指标、配对统计和运行时审计

- 实现评分与配对统计，修正指标口径和配对校验。
- 实现追加事件日志、原始blob哈希、状态快照与回放接口；字段白名单不等于操作系统权限隔离。
- 测试目录、失败记录和证据目录按用户要求保留，不自动删除。
- 主要位置：`cocoon/metrics.py`、`cocoon/runtime.py`、`tests/test_metrics.py`、`tests/test_runtime.py`。
- 对应任务：11–20。

### 步骤05｜2026-11-07至08：冻结原助手并建立无回退适配层

- 保存原始zip、入口HTML和来源记录；提取并静态冻结原助手提示词。
- 建立严格JSON阶段契约、引用ID校验、失败停止与完整原响应留存。
- 五阶段：`search`、`label`、`blindspot`、`integrate`、`mirror`。受控模式的search仅梳理冻结证据，不是在线检索。
- 原件：`vendor/cocoon-breaker-original/`。
- 适配代码：`cocoon/assistant.py`、`cocoon/contracts.py`、`cocoon/prompts.py`。
- 提示词：`configs/assistant_prompts_v1.json`；bundle内容哈希为 `c16363a126daa1d36c83cfdb247003f9191420c64be80a0e0308d9c3edb7af26`。
- 最终一次离线场景验收：13/13通过，31次夹具调用，真实模型调用0次，原助手文件未变。
- 记录：`experiment/adapter_checks/adapter_20261108T063210_0b9b487a/`。
- 对应任务：21–24。

### 步骤06｜2026-11-08：接入MiMo传输与累计预算保护

- 核对官方API模型ID、请求地址、鉴权方式、输出token参数、思考模式和国内实时价格。
- 采用 `thinking=disabled`、温度0、助手输出上限4096；连通测试单独限制128。它们是小规模探测设置，非正式实验参数冻结。
- 加入官方地址白名单、默认TLS校验、禁止重定向携带凭据、无自动重试、无模拟回退。
- 预算账本使用Decimal、文件锁、追加哈希链；请求前保守预留，按usage结算；用量不明不释放预留并阻止继续。
- 修复不完整JSON及二次编码凭据的潜在留存问题，响应不能安全保存时仅保留摘要、长度和原因。
- 代码：`cocoon/mimo.py`、`cocoon/budget.py`、`cocoon/mimo_probe.py`。
- 累计账本：`experiment/billing/mimo_initial_probe_v1.jsonl`，不得靠删文件或换路径重置预算。
- 该阶段全量离线回归最终406项通过；曾有不完整JSON留存旧断言失败，修正后通过，失败报告保留。
- 对应任务：25–28。

### 步骤07｜2026-11-08 14:55：真实连通性通过

- 临时进程凭据完成一次调用，模型返回 `{"connection":"ok"}`。
- 45输入＋6输出＝51 tokens；保守记账¥0.000057。
- 运行：`experiment/mimo_probes/connection_smoke_20261108T065524_5ca1d2cb/`。
- 没有启动助手完整任务或正式实验；进程结束后没有把凭据持久化到项目配置。
- 对应任务：29。

### 步骤08｜2026-11-08 15:11后：恢复原方案，继续原定三个方向

- 微信临时目录中的原方案此前无法读取，用户将文件放回 `D:\信息茧房`。
- 核对字节长度56255、SHA256与历史记录一致；在 `core.json` 登记稳定项目内路径。
- 按第4.3节的碳与气候、能源转型、中文公共信息核查制作候选，不使用先前临时建议的教育主题。
- 搜索连接器授权失败且被跳过，未继续重试该连接器；公开来源使用可用的搜索与网页取证方式，受限页面不绕过。

### 步骤09｜2026-11-08：保存真实来源并制作18条候选证据

- 保存入选13个HTML页面、提取文本、来源、发布日期、抓取时间及哈希；18条中文释义均明确为翻译摘编或中文摘编。
- 三议题各6条；生成3个完整候选包及6个两轮切分草案。切分不是T1个性化检索结果。
- 能源成本部分一手页面返回403，改用已标明层级的二手转引；同一报告的转引共享来源家族，不计作独立研究。
- 中文公共核查候选收窄为天气信息；不是CHECKED原始社交条目，也没有伪造历史错误消息。
- 独立AI审核发现CL_E05引文未直接覆盖“仍呈碱性”，已更换为同页连续片段；补明历史日期，保留初审与复核记录。
- 全部18条引用精确匹配，哈希检查通过；人审仍0，权利状态未自动批准。
- 产物：`experiment/evidence_candidates/v1_20261108/build_20261108T074108_f38ec5/`。
- 来源底稿：`experiment/evidence_candidates/v1_20261108/intake/`。
- 新代码：`scripts/capture_evidence_source.py`、`cocoon/evidence.py`；来源全文未装入外发压缩包。
- 对应任务：30–32；该阶段全量回归415项通过。

### 步骤10｜2026-11-08：发现旧显示方式挤占阅读预算

- 原显示包含完整URL和冗长来源族ID，六个证据块分别为729、835、794、759、725、767字符。
- 其中835已超过800，其他多轮也几乎没有空间附加组织、反思或复述。
- 没有删证据、改上限或把仅折叠HTML说成实际输入变短；改为登记新的受试输入显示版本。

### 步骤11｜2026-11-08：形成等证据剂量编辑设计稿

- 新显示规则 `source_id_inline_v1`：正文原样保留，显示证据ID、来源ID、机构短名与文献日期；完整URL及家族仅供审核映射。
- 明确这是真实输入格式改变，非纯UI优化。受试上下文不隐式附加审阅链接，也不新增浏览机会。
- 建立总长与附加段双重匹配、相同公共回应提示和一次回应机会。
- 编写6对编辑草稿，独立AI审核通过其限定范围；不把编辑稿当成小米原助手输出或个体镜像。
- 修复配对清单重复轮次及虚假汇总仍可被验证的问题，加入回归测试。
- 12份消息均为690–796字符；最大总长度差约1.14%，最大附加段差约3.91%。
- 代码：`cocoon/dosage.py`、`cocoon/dose_build.py`；稿件：`configs/dose_additions_v1.json`。
- 验收版：`experiment/dose_candidates/dose_20261108T081317_cf1bb3/`；较早构建保留，不再作为当前验收入口。
- 对应任务：33–36；该阶段全量回归478项通过。

| 议题 | 第一轮I4侧 / I5侧完整字符 | 第二轮I4侧 / I5侧完整字符 |
|---|---:|---:|
| 碳与气候 | 690 / 691 | 691 / 693 |
| 能源转型 | 727 / 722 | 715 / 711 |
| 中文公共信息核查 | 745 / 739 | 787 / 796 |

### 步骤12｜2026-11-08 16:21–16:22：第一次真实四阶段助手任务

- 输入：`CAND_TOPIC_01_R1_V1`，三条碳与气候冻结证据。
- 四阶段全部完成并通过结构校验；不含镜像，不使用虚构T1观点。
- 4次HTTP调用，15729输入＋3387输出＝19116 tokens；本轮保守记账¥0.022503。
- 原运行：`experiment/mimo_probes/assistant_probe_20261108T082120_9ad78cf8/`。
- 已保存29项事件、47个blob；通过原HTTP、请求上下文、阶段结构、提示词和引用关联独立重放核验。
- 对应任务：37–38。

### 步骤13｜2026-11-08：真实输出暴露语义问题与投递缺口

- 独立AI逐项审核39项：11项证据支持、17项合理缺口或问题、3项缺乏支持的事实、8项过度断言；共11项问题，非人工最终裁决。
- 主要问题：从机构名推断权威/立场；将机制事实升级为行动偏好；无观点数据却推断用户采信倾向；把不能推断强化为结果不能发生。
- 整合报告完整渲染1594字符。若直接拼入证据和公共提示，候选共2051字符，不符合最终投递目标。
- **纠正口径：长内部报告本身不受800目标限制；问题是不能直接把长报告当最终受试材料。** 该2051候选没有发给受试Agent。
- 未删问题项、未截断报告、未重调以筛选有利结果；旧原始输出完整保留。
- 审计代码：`cocoon/live_audit.py`；语义记录：`experiment/review/live_semantic_20261108.json`。
- 阅读页：`experiment/review/assistant_live_20261108/review.html`。
- 曾有测试错误地预期真实整合报告必含完整URL；实际报告未输出这些URL，已改为按真实内容核对，并另用隔离夹具检验URL保留，不捏造真实命中。
- 对应任务：39；该阶段全量回归506项通过。

### 步骤14｜2026-11-08 16:50后：确认按原方案分离长报告和短投递

- 用户明确选择“原实验方案”：长内部报告继续保留，独立生成600–800的最终投递材料，不把800改成模型输出限制。
- 新建短投递契约：组织反思侧可读取不可信内部报告与同一证据；普通复述侧只读共同证据和长度目标，不读另一侧正文或内部长报告。
- 约束新增事实、机构权威推断、个体诊断、事实与立场混淆、主要/可能/不能推断等语气强化。
- 新文件：`configs/delivery_prompts_v1.json`、`cocoon/delivery.py`、`tests/test_delivery.py`。
- 提示词字节SHA256：`293fa2e89f55b426f708febd211653273cbbf378e21a6cedfab70ebfc0375372`。
- 该模块单独30项离线测试报告通过；**加入此模块后的全项目回归尚未运行**，不能把此前506通过自动视为当前全部代码已通过。
- 无T1仍不生成个性化镜像；当前是短投递管线探测，不是完整I4。
- 对应任务：40–42，仍未完成。

### 步骤15｜2026-11-08 17:05：短投递v1真实尝试失败

- 只执行一次组织反思段请求，模型返回的附加段（含引用标记）403字符，超出本次225–245。
- 即使只检查原方案允许的143–343附加空间，也超出60字符；因此不是单纯把内部目标放宽就能认定达标。
- 程序停止，保留原响应；没有请求普通复述侧，没有成功配对，没有实际受试投递。
- 本轮2621 tokens、¥0.002959；父四阶段运行与长报告不变。
- 运行目录及确切错误见本文件第1节。
- 本次命令已结束，不再标为后台运行中。后续版本不得覆盖它或将其改写成成功。

### 步骤16｜2026-11-08：记录尚未修复的代码审查项

- 对 `cocoon/delivery.py` 的只读审查发现P2：每次请求前检查父运行、packet、manifest、policy，但最终状态前仅核对父运行与内存报告。
- 若最后一次HTTP在途时packet、manifest或policy被修改，现实现可能仍报告成功；这是冻结输入的末次检查窗口缺口。
- 建议：终态前重复完整输入校验，失败时保留已有响应并标为 `source_changed`；用隔离测试覆盖。
- **截至本记录尚未修复**，不能写成已完成。当前真实尝试在第一阶段因长度失败；审查发现不等于实际发生了文件篡改。

### 步骤17｜2026-11-08 17:08后：建立本进度日志

- 用户要求用Markdown保存每一步与进度，本文件首次补录历史并建立持续追加方式。
- 重新读取最近短投递summary及计费台账，核验7项事件/17个blob后写入实际失败状态和费用。
- 更新任务40、41的描述，保留进行中；任务42待处理，不因已写代码或只做了一次尝试就自动标为完成。
- 本次仅做进度归档，**未新增模型调用，未修改原始运行、证据或原方案**。
- 日志核验已完成：17个步骤、文内3个相对链接均有效；费用和token汇总与6条结算记录一致；未发现密钥格式内容。

### 步骤18｜2026-11-08 18:13：修复冻结输入校验并登记短投递v2

- 已读本日志接续任务40–42，没有重做之前的证据与长报告。
- 修改 `cocoon/delivery.py`：统一在发送前、响应原文保存后及终态前复核父运行、证据包、清单、提示词与来源表；任一变动保留原响应并停止。报告是否改变与其他输入是否改变分别记录，不混淆。
- 保留v1政策和失败记录，新建 `configs/delivery_prompts_v2.json`，哈希 `467ee4908f3dea92f443369b2c24deb0e4c8606a9d4b2caf6f221b79bd7347b5`。
- v2不再把225–245当成额外验收目标；首段采用最终600–800扣除固定457之后的143–343空间，235仅为生成目标。
- 四句分别绑定CL_E01、CL_E02、CL_E03、CL_E03，每句只含一个引用。当前首段正文预算28–64字符/句、目标51，引用共32字符；次段再按首段实际长度计算10%配对预算，且不读取首段正文或内部报告。
- 52项投递模块离线回归已通过（含末次修改packet/manifest/policy/来源表的拦截与v1兼容）；实际v2配置加载及预算计算已核验。新增代码后的全项目回归仍待本轮最后执行。
- 截至本步骤没有新增收费调用；下一步仅进行一次v2真实小规模探测，失败保留，不自动重试。此版本不等于完成T1或个体镜像。

### 步骤19｜2026-11-08 18:14：短投递v2实际尝试，首侧通过、次侧失败

- 运行：`experiment/delivery_probes/delivery_20261108T101439Z_99cfd0db64294c3a8c51b1248b03eb98/`，实际执行2次HTTP，两次均收到响应和usage。
- 组织反思侧结构与分句预算通过；附加段173字符，加原样证据与公共提示457字符，共630字符，达到最终600–800目标。
- 普通复述侧在严格契约检查中失败：模型返回数字 `schema_version: 1.0`，契约要求字符串 `schema_version: "1.0"`。未将数字静默转换为字符串，也未把失败输出用于正式配对；其他句长问题须继续做只读诊断。
- 终态 `delivery_failed`，阶段 `delivery_plain`，错误 `invalid_schema`；只通过1个投递阶段，尚无合格配对。两次原响应保留，没有自动重试。
- 新增用量：3679输入＋355输出＝4034 tokens；本轮保守记账¥0.004389，累计¥0.029908，剩余¥4.970092，无未决费用。
- 父运行、原长报告、证据及冻结输入均复核未变；13项事件、27个blob，哈希链有效。
- 后续：独立审阅两侧实际原文并记录全部诊断；本次不再发起另一轮收费请求，不用局部成功冒充整体通过。

### 步骤20｜2026-11-08：v2原始输出重放、语义复核与失败定位

- 新增 `cocoon/delivery_audit.py`，从原始HTTP、请求ID、冻结输入、逐阶段事件和summary重建v1/v2结果；成功响应但结构失败的文本只作诊断，不转换类型、不补字、不生成有效I5。
- 12项只读审计测试通过，覆盖原文、费用快照差值、v1/v2失败、错误类型保留、跨请求关联及防篡改；该审计不证明外部网络真实性或供应商最终账单。
- 3项审阅页及语义绑定测试通过。逐8句的AI意见绑定原响应和packet哈希，7句支持、1句合理问题；内容通过不解除结构失败。
- 已确认普通侧前三句29、29、30字符，第四句37；要求每句32–39。正文125加引用32等于157，总候选诊断614；附加段差16/157约10.19%，超过10%。
- 原提示“schema_version等于1.0”存在类型表达歧义；后续版本应明确带引号字符串。当前版本和两个原回复不改，不把过错都归咎于模型。
- 更新 `configs/core.json`，记录v2真实失败和首侧630通过，正式资格仍false；原来四阶段的11项语义问题及旧报告记录保持原样。
- 审阅材料：`experiment/review/delivery_v2_20261108/`；逐句AI记录：`experiment/review/delivery_v2_semantic.json`。
- 本次重放和审阅新增收费调用0；v2试跑后没有再发模型请求。全项目回归结果在下一条验收记录补充。

### 步骤21｜2026-11-08 18:43：全项目回归完成

- 执行 `python -m cocoon validate`，573项测试全部通过，失败0、错误0、跳过0。
- 报告：`experiment/review/validation_20261108T104347_89f97d.json`。
- 覆盖v1/v2投递、末次输入检查修复、失败原文重放和审阅页；程序测试通过不改变v2实际配对失败。
- 下一步仍是修订新版本的schema字符串写法和普通侧句长生成规则；本轮没有进一步收费尝试。

### 步骤22｜2026-11-08 18:55：预登记短投递v3，仅修提示表达

- 读取本日志和v2失败记录后继续；不重建证据、不改原报告、不改失败输出。
- 新配置 `configs/delivery_prompts_v3.json` 明确 `schema_version` 必须为JSON字符串 `"1.0"`；每句分别按正文字符闭区间检查，目标不是上限，不足时仅补原证据已有条件，不用空白或重复内容凑字。
- 所有数字门槛继承v2：最终600–800、总长及附加段10%、四句算法、引用开销、最大1024输出tokens、无重试不变。v3并未通过放宽阈值让v2失败变成功。
- 修改 `cocoon/delivery.py` 和 `cocoon/delivery_audit.py` 注册v3但保持v1/v2兼容；v3政策文件SHA256：`b2cecda52c4fa2725400063094dcee9466a16037e02bfa05f64fcf883d744684`。
- 投递模块58项离线测试通过，新增覆盖v3精确类型写法、两阶段预算、普通侧隔离以及数字版本仍被拒绝。
- 真实请求前额度快照：累计¥0.029908、剩余¥4.970092、无未决预留。本轮预先限定只执行一次v3双阶段尝试，失败即停；之后只做离线审阅，不再连续收费抽样。

### 步骤23｜2026-11-08 18:55–18:56：v3真实试跑解决类型问题，但句长仍失败

- 运行：`experiment/delivery_probes/delivery_20261108T105552Z_7fe7dae9d342459885c811b169a74ff1/`。
- 两侧schema_version均为字符串"1.0"，v2类型歧义在本轮实际响应中已消除。
- 组织侧附加175、完整632字符，通过；普通侧附加155，低于160–192要求，前三句31/28/27字符低于32下限，首错为length_out_of_range。完整612只作诊断，不是已接纳的I5。
- v3仍为delivery_failed，未生成合格的双模型配对。没有改类型、补字、截断或再次抽样。
- 本轮2次HTTP，4185输入+356输出=4541tokens，记账¥0.00439524；本次存在缓存命中，费用不再可直接按所有输入均未命中计算。累计¥0.03430324，余额¥4.96569676，无未决预留。
- 原报告和全部冻结输入未变；独立AI对8句复核为7句支持、1句合理问题，不豁免结构/长度错误。

### 步骤24｜2026-11-08 19:18后：停止收费试错，构建单独的整句摘录式对照备选

- v3之后未再调用模型。不再只加长提示词期待模型精确计字，转为离线研究可重复的普通阅读实现。
- 新增 `configs/extractive_control_v1.json` 与 `cocoon/extractive_control.py`；哈希 `b96e2a12d9b85189e6765c0aa23b04a6f2ad2bec6d57a8d73194d34c2fe5413a`。
- 保留组织侧175字符真实原输出；对照侧只从同一冻结包每条证据选一个完整原句，不改字、不加连接语、不读组织侧正文来选句。仅以相同长度预算，按证据顺序与句偏移字典序选择第一个合格组合，保存全部8个组合的长度诊断。
- 选中句索引0/0/1；摘录段180字符，完整637字符。与组织侧632相比，总长差约0.79%，附加段差约2.86%，共同证据块和来源、回应提示相同，结构/剂量检查通过。
- **这是新的事后探索性备选，不是修复或重新认定v3成功。** 对照内容来源明确为deterministic_exact_source_sentences，不冒充小米生成。组织四句、对照三句是新增实现差异；原方案共同证据数量与最终阅读量仍相同，正式采用需重新登记。
- 独立AI审阅18项检查通过其限定范围；人审仍0，无T1/完整I4，不发给受试Agent。15项摘录模块测试通过。
- 文件：`experiment/review/delivery_v3_20261108/extractive_alternative.json` 和 `extractive_review.json`。v1/v2/v3实际失败记录全部保留。

### 步骤25｜2026-11-08 19:35：全项目回归与分层交付

- `python -m cocoon validate`实际完成603项测试，失败0、错误0、跳过0；报告 `experiment/review/validation_20261108T113453_b8882e.json`。
- 新增通用版本审阅页，数据从实际记录读取，不将v2的630/614或类型错误硬编码到v3；v3类型已正确、原配对仍失败如实展示。
- 交付分别呈现v3原失败审阅和独立摘录备选。备选对照不由模型生成，不覆写v3状态，不把结构匹配升级为正式批准。
- 新增和变更包括 `configs/delivery_prompts_v3.json`、`configs/extractive_control_v1.json`、`cocoon/delivery.py`、`cocoon/delivery_audit.py`、`cocoon/extractive_control.py`、`cocoon/reporting.py` 与对应测试。
- 本轮已累计10次真实请求、¥0.03430324；摘录备选及其审阅新增真实调用0，v3之后没有追加模型请求。
- 可重复重建的备选已完成当前案例的离线验证；下一步是确认是否采用该对照实现，再核验其他案例与真实T1/镜像，不能直接启动正式实验。

### 步骤26｜2026-11-08：完成六轮整句摘录离线可行性检查

- 对三个议题、每题两轮的冻结证据枚举完整句组合；不修改证据、不生成缺失的组织侧回复、不调用模型。
- 六轮均存在满足最终600–800字符及两侧10%匹配要求的长度组合。组织侧附加段可匹配范围分别为：碳与气候R1 143–234、R2 141–214；能源R1 145–257、R2 141–238；天气核查R1 132–205、R2 140–227字符。
- 这些范围指附加段，完整输入还包括固定证据、来源、标题与回应提示。539/1206是可匹配整数长度的覆盖，不是模型成功率。
- 只有碳与气候R1绑定既有632/637字符探索性备选；其他五轮只是条件可行，没有真实组织侧或实际配对。
- 扩展 `cocoon/extractive_control.py`；新增 `tests/test_extractive_feasibility.py`，18项专项测试通过。
- 结果：[六轮可行性数据](experiment/review/cross_topic_20261108/feasibility.json)。本轮新增模型调用0，费用0。

### 步骤27｜2026-11-08：整理未填写的双人审核清单

- 新增 `cocoon/human_review.py` 与 `tests/test_human_review.py`；12项专项测试通过。
- 清单包括18条证据、13个来源、原报告11项AI问题、6轮语境检查和7项放行门槛，共55项、110个人工审核位。
- 审核者身份、时间和意见保持空值或pending；人工完成0，未作人工裁决，不自动批准。原报告问题文字、引文、来源及文件哈希保留绑定。
- 结果：[双人审核清单](experiment/review/cross_topic_20261108/human_review_checklist.json)。这是待填写模板，不是已通过审核的正式材料。
- 截至20:12补发结果时，以上两模块30项专项测试通过；本轮可读页面及完整交付收尾尚未完成，不把旧603项全项目测试说成包含本轮修改的新回归。
- 累计费用沿用¥0.03430324，余额¥4.96569676。下一步完成审阅呈现与验证，再安排真实人工核查；不启动正式实验。

### 步骤28｜2026-11-08 20:19–20:35：修复独立审阅绑定兼容，完成离线交付

- 执行用户转达的Gemini收尾指令；本轮仅本地修复、测试、生成页面与登记，不发起模型或API请求，新增费用0。
- `cocoon/reporting.py` 的 `render_cross_topic_review` 同时接受顶层 `feasibility_file_sha256/checklist_file_sha256` 和 `input_sha256` 中 `feasibility.json/human_review_checklist.json` 的绑定。两种同时出现时必须全部匹配，缺项、结构错误、冲突及原字节改变都拒绝。
- 继续严格要求 `review_type=independent_ai_not_human`、`human_reviews_completed` 为整数0、`formal_eligible is False`，不接受布尔False冒充计数0或数字0冒充正式资格False。
- `tests/test_cross_topic_reporting.py` 增加6项测试，包括真实落盘独立意见渲染、字节与JSON值区别、双格式冲突、缺项/无效结构、身份与资格检查和渲染期间变更。11项审阅页专项测试通过；旧报告代码前116782字节哈希未变。
- `python -m cocoon validate` 于20:34完成：**644项测试、0 failures、0 errors、0 skipped、success=true**。报告：[最新全项目验证](experiment/review/validation_20261108T123445_bbef07.json)。日志确认含18项 `test_extractive_feasibility`、12项 `test_human_review`、11项 `test_cross_topic_reporting`。
- 使用最新测试结果与原 `independent_review.json` 生成静态只读 [review.html](experiment/review/cross_topic_20261108/review.html)。页面含6轮范围、41句及72组合、人审55项110位和独立AI语境意见；无脚本、表单、自动联网或填写持久化，支持打印。
- 既有独立意见状态为 `pass_with_context_review_required`，列出6项人审优先关注；这里只修复绑定及呈现，没有新做模型语义判断，也没有将AI意见提升为人工批准。
- 三份受保护原件 SHA-256 保持不变：feasibility `5ff1b33d1115f5b9cfccfe0c89da2eac91dc1477421c11d553c8b15a5cfd5d55`；human_review_checklist `fd2d9adde69f478544a41061f83137f78fc925618046b0791478715398040706`；independent_review `61dbdb91b676b6da7f27459f6a5f993785e8dd829aa84cf9daee5230ddcb8831`。
- 更新 `configs/core.json` 的 `cross_topic_review` 路径、哈希、测试记录和限定状态；保持人审0、formal_eligible=false、formal_launch_enabled=false。第1/5/6节同步，历史任务45/49按实际任务表保留进行中，不代替本轮结案。
- 本轮独立汇报：[REPORT_step28_20261108.md](experiment/review/cross_topic_20261108/REPORT_step28_20261108.md)；交付清单 `experiment/review/cross_topic_20261108/delivery.json`；离线包 `experiment/exports/cross_topic_closeout_20261108.zip`，不含原始网页全文或凭据。
- 本轮累计账本字节未变，SHA-256 `e6d0168f0d8a80988ad8d322843695f86d9d1ba4899be8ea330538b409861931`；累计¥0.03430324、余额¥4.96569676不变。下一步等待用户转达的新指令，真实双人人审、T1与完整I4仍未完成。

### 步骤29｜2026-11-08 22:04–22:35：实现双人独立审核副本核验与第三人裁决

- 执行用户转达的步骤29指令；仅扩展 `cocoon/human_review.py`、新增 `tests/test_human_review_workflow.py`，原模块前25853字节未改，旧三个空白模板接口保持行为。
- 新公共API `merge_and_verify_human_reviews` 与 `verify_human_review_submission` 重建权威模板、核对55项不可填字段/来源哈希/检查键，严格区分两独立副本的可写槽位，不接受越权修改对方意见。
- 已完成槽检查ID、带时区ISO时间、非空意见和全bool检查值；拒绝机器标识、同人双签、跨条目角色交换、第三人与全局审核集合重叠、False检查却作通过决定。
- 双槽决定或任一check不同自动产生分歧，待裁决不计最终完成/通过。第三人不得改原意见；check分歧须给出完整bool裁决checks，仅决定不同且check一致时可沿用一致检查。
- 计数全部重算，区分完成槽、双槽完成、已解决条目、分歧、裁决、通过/需改/拒绝。前48项通过不代替7项gate；当前full_108_card_review=False，因此即使全部55项通过仍formal_eligible=False。
- 39项专项内存夹具测试通过，未将任何模拟签署写成正式文件；真实模板人审仍0。ID格式校验不是实际身份认证，返回identity_verified=False。
- 首次全项目回归 `experiment/review/validation_20261108T142436_14949a.json`：683项、0失败、4错误；4处为旧adapter检查在新测试目录追加事件文件时的Windows PermissionError。只读ACL/属性检查后，旧模块原样单独6项通过，暂未复现，未改权限、未删目录、未改运行时；未修改生产/测试代码原样再次全回归，最终 `experiment/review/validation_20261108T143449_f6add9.json` 为**683项、0 failures、0 errors、0 skipped、success=true**。包含本轮39项、旧人审12项/可行性18项、跨轮页11项和旧adapter6项全部通过。写入错误具体占用原因未确认，若再出现须独立诊断。
- 本轮独立汇报：[REPORT_step29_20261108.md](experiment/review/cross_topic_20261108/REPORT_step29_20261108.md)，包含公共API约定、计数定义、裁决格式、首次失败及最终回归记录。更新core最新validation指针与工作流登记；真实human_reviews_completed=0、formal_eligible=false。
- 原 `human_review.py` 前25853字节SHA-256仍为 `b93cfab68063c236f6d0b70aa5f209130bf4aaec40fd9a41aab2af33ff4fb846`。六份步骤28原件及账本逐项复验字节不变，没有生成任何已填人审正式文件；新增网络/模型调用0、费用0。
- 验证只证明源绑定、填写格式、声明的独立性及流程计数，不证明不同ID背后是不同真人；需要实际身份来源核验。旧模板的检查键没有改极性，通过仍按用户要求所有True，不自行将问句反转。
- 最新报告SHA-256：`c3017ef178e7f664e423ae5752528cb09e514e54b1eabb37f4b38a57361bbd5a`。下一步等待用户转达新指令或真实审核副本，不自动签署、不启动正式实验。

### 步骤30｜2026-11-08 22:50–23:08：实现测量隔离、盲评与自报桥接契约

- 新增 `cocoon/measurement.py` 与 `tests/test_measurement.py`，不改metrics/runtime/contracts/scheduling/human_review等旧模块及步骤28/29产物。没有模型/API/网络调用，新增费用0。
- 公共问卷严格8锚题、可选0或4迁移题；每题仅ID/纯文本命题，私有真值与6维/量规单独校验，金标准真值拒绝bool。所有正式题目真值均未生成或落盘。
- 从runtime.measurement_view深拷贝适配指定Agent，只采信其显式exposure_delivered/delivered/sent_to_model=True记录提取已见ID；其他人、库存与prepared_inputs不计入。不改原消息、记忆或世界状态，外层审计字段不发送。
- 严格解析附录B JSON，允许缺题但不补概率，拒绝未知引用/重复键/非有限数/HTML与敏感键。桥接拼接所有自报理由和已知/待查/异见说明原文，精确连续子串可用于mirror.user_quote核验。
- 本地方案不存在§8.5，且第8节要求自然T1来自常规发言。本轮按任务实现测量自报桥接，但明确subject_measurement_extracted、natural_routine_speech=False、requires_protocol_review=True、formal_eligible=False，不将自报字符串包装成真实自然发言。
- 盲评实际包仅blind_sample_id、evidence_notes、opposing_view、dimensions、opposing_rubric；不含answers/p_true/gold_answers或时点/分组。显式I4/T3/world_id等污染拒绝，不静默删改文本。
- 盲评分维度原序6项、严格bool、引文须来自受试notes的单字段精确子串。mastered优先，recognized_gap只计未掌握；U三项严格整数0..2。
- 直接复用metrics：锚题分母8与迁移分母4分开；缺题BS/Acc/S为None且保留上下界，缺盲评O/U为None。正式资格和实际观测验证均false。
- 40项合成内存专项测试通过，含mirror端到端；全项目 [validation_20261108T150756_1871ae.json](experiment/review/validation_20261108T150756_1871ae.json) **723项全部通过、0 failures/0 errors/0 skipped**，无正式受试/金标准夹具落盘。
- 本轮汇报：[REPORT_step30_20261108.md](experiment/review/measurement_20261108/REPORT_step30_20261108.md)；core登记8个API对应模块及最新验证路径，PROGRESS更新顶部与第5/6节。步骤28/29所有保护原件与账本逐项字节校验一致。
- 下一步待上层真实状态/事件桥接、匿名ID映射与测量自报使用边界确认。ID/哈希/脱敏字段检查不是实际身份、真实送达、语义正确或完整双盲保证。

### 步骤31｜2026-11-08 23:27–23:55：常规发言桥接、匿名注册与盲评回填

- 仅在measurement.py原27765字节之后追加新3API，旧8API及测量自报备选行为不变；扩展tests/test_measurement.py至66项，不改runtime/contracts/metrics/extractive_control等旧模块。
- 新 `extract_t1_routine_speech_view` 从T1第8轮快照的routine_speech_history读取指定Agent已生成曝光发言，拒绝测量/系统/私有标签/空白/未生成/未来记录。其他人和其他议题排除，按轮次逻辑序取最近完整条目并记录排除ID，零写回，user_quote逐字追溯。
- 常规通道标subject_routine_speech、natural_routine_speech=True、requires_protocol_review=False；这只说明来源契约对齐原方案，不认证实际生成观测。旧subject_measurement_extracted通道仍为测量自报备选，不相互替代。
- 新 `create_blind_sample_registry` 在局部seed随机流上打乱样本并分配BLIND_0001类中性ID，public_blind_packets是唯一可发Evaluator的字段；source_entries、条件/个体/时点映射及整体hash仅控制器私有。
- 新 `reconcile_blind_evaluations` 重建registry并核对整测量、问卷/gold、匿名包及评估响应；未知/重复/串样本拒绝，部分评估保留全部样本与客观分，O/U缺失为None，8锚题/4迁移分别计分。支持可信控制器外存expected_registry_sha256阻止整包改写，未提供不冒充可信签名。
- 66项专项通过，含两隔离分支的常规发言→mirror→整句摘录配对→T2测量→匿名盲评→面板回填。项目不存在build_extractive_control或analysis.py，测试改用已有select_exact_sentences与runtime.make_intervention_pair，不伪造旧真实运行入口；面板仅个体长表，不假称已完成网络统计。
- 第一次全回归validation_20261108T154323_08d340.json为749项全部通过；随后加强第64项测试中的两分支阅读输入连接和实际信封字数，再跑完整回归，末次 [validation_20261108T155515_46ef93.json](experiment/review/validation_20261108T155515_46ef93.json) 为**749项、0 failures、0 errors、0 skipped、success=true**。多行文本单行JSON信封只作内存契约测试，额外字数重计，不改冻结投递格式。
- 本轮未创建真实发言/registry/金标准或面板结果文件；独立汇报：[REPORT_step31_20261108.md](experiment/review/measurement_20261108/REPORT_step31_20261108.md)。步骤28/29/30原件及账本保持字节，新增模型/API/网络调用0，费用0。
- core登记常规桥接/registry/面板契约与最新回归；未把配置中的natural_routine_speech标志当成已有真实观测。报告SHA-256为538fb6be668bf3c70fead7670ca3e8908acb1e0215788496a68b2ea2145b38ff。

### 步骤32｜2026-11-09 02:40–10:56：网络级聚合、2×2曝光、配对干预与实际槽位随机化检验

- 新建 `cocoon/analysis.py` 与 `tests/test_analysis.py`，不改metrics/runtime/contracts/scheduling/measurement/human_review/extractive_control/reporting等旧模块及步骤28–31产物；无模型/API/网络请求，新增费用0。
- `aggregate_panel_to_networks` 严格核验步骤31面板封装与逐行哈希，按 `(topic, block, world, environment, arm, timepoint)` 聚合；`expected_agents_per_world` 沿用 `scheduling._check_population_size`（整数≥8且4的倍数）。仅全员且指标完整时给精确网络均值，否则 `valid=False`、精确值None；`BS_lower_mean/BS_upper_mean` 始终按固定期望人数分母，缺失个体按0/1极值，绝不静默剔除后冒充完整网络均值。8锚题与4迁移题分开保存。
- `analyze_exposure_2x2` 取A/B/C/D的T0–T1网络变化，核验同世界条件一致，直接调用 `metrics.exposure_contrasts` 输出同质、错误信息、交互效应；BS另给极值上下界。若面板同时有未分配臂曝光网络与干预臂T1行，只取前者并记 `exposure_arm_scope`，是阶段选择而非丢弃缺测。
- `analyze_intervention_effects` 校验六臂共享T1（≤1e-12）、统一归一化损失后调用 `metrics.paired_summary`；主比较I4_vs_I0/I4_vs_I5标primary_confirmatory，I1/I2/I3/I5_vs_I0标secondary_exploratory；效应与ci_95按原量纲还原并保留归一化原值。支持T2/T3终点、Acc/U等方向及非BS边界不适用标记。
- 随机化检验只接受可经 `scheduling.allocate` 重建、且与网络记录槽位/臂/世界/环境一致的allocations；在每个完整有效区组内置换六臂标签，两项比较各自独立计统计量，按 `(1+count(|stat_perm|≥|stat_obs|))/(1+reps)` 给 `p_raw`，调用 `metrics.holm` 给 `p_adjusted`。无allocations时p全为None；有缺测区组时确认性估计限定同一批完整区组并标 `conditional_on_complete_blocks_only`，不把条件p值冒充全样本检验。
- 专项测试22项通过：完整/缺测网络与手算边界、人口规模与篡改拒绝、demo门禁、d_A..d_D与算子一致、干预臂T1隔离、共享T1拒绝、p值None/置换/Holm/8类allocation篡改、T2与Acc、输入不变，以及由 `reconcile_blind_evaluations` 到曝光2×2的64条合成测量闭环。
- 末次全项目 [validation_20261109T025602_582dd0.json](experiment/review/validation_20261109T025602_582dd0.json) 为**771项、0 failures、0 errors、0 skipped、success=true**；含test_analysis 22、test_measurement 66、test_human_review_workflow 39等模块。
- 独立汇报：[REPORT_step32_20261108.md](experiment/review/measurement_20261108/REPORT_step32_20261108.md)。core新增 `network_analysis` 段并更新最新验证指针与stage；`formal_launch_enabled=false`、人审0、正式资格false。
- 步骤28–31九份受保护原件、计费账本、原方案哈希逐项复验不变；`measurement.py` 前27765字节旧8API前缀保持。注：步骤31汇报当前实际字节SHA-256为 `b7a08c7bd2e5a1ff408782fb071e75834c42e5247a38893ee3498d86b4710c17`，本日志步骤31段所记 `538fb6be…` 为写制中间值，本轮未改该文件。
- 局限：`metrics.holm` 实际签名是dict→dict而非列表，按真实接口调用；`metrics.exposure_contrasts` 无demo门禁，合成演练用受控克隆并在外层恢复is_demo/formal_eligible，不改旧算子。自含哈希不是外部签名；真实面板、可信匿名摘要、双人人审与正式预实验仍未执行。

### 步骤33｜2026-11-09：TOPIC_01 Pilot 三区材料包与§5.2模拟审核演练

- 新建 `cocoon/pilot_materials.py` 与 `tests/test_pilot_materials.py`，纯标准库离线实现；只读 `experiment/evidence_candidates/v1_20261108/build_20261108T074108_f38ec5/`，不写正式材料文件，不改步骤28–32产物、账本或空白人审模板。新增模型/API/网络调用0、费用0。
- `build_topic01_pilot_materials` 先 `evidence.verify_bundle` 核验候选构建，绑定 `CL_S01`–`CL_S04` 的URL、获取时间、raw/text SHA-256、来源族与权利状态，以及 `CL_E01`–`CL_E06` 的连续英文引文和中文释义。
- 区域1：§5.1精确配额的72张曝光卡＋36张保持卡，6分层（立场±1/0 × 准确/摘编误读）分别为16/8与8/4；`card_id` 前缀 `T01EXP_`/`T01RET_` 严格分开；每张卡受试可见文本180–220字符、标 `translated_adapted`、保留 `original_quote`，经 `scheduling.public_card` 导出后只剩7个白名单字段。错误卡的"待辨析历史常见外推主张"说明仅放控制器私有 `controller_note`，不向受试标真伪、不冒充NOAA/NASA认可结论。
- 排程：A/B/C/D × 初始立场±1 × seed0–5 × 曝光8轮/保持4轮共96次 `schedule_cards(max_repeats=2)` 全部成功，每轮6张、单卡单次排程重复≤2，逐次重算记录；未通过改seed或错误分布迁就库存。
- §6.4：8＋4共12个冻结讨论槽（`generated_live=False`、不实时转发给其他受试），另有预定义空白讨论兜底。六臂两轮12份干预候选包全部600–800字符、两轮合计1200–1600、单次回应机会、不含I4/I5字样、不跨用保持库存；I0–I3只用原证据整句的确定性摘录且8份附加文字互不相同，I4/I5用 `dosage.make_dose_pair` 装配TOPIC_01 R1/R2等证据编辑稿（R1 690/691、R2 691/693）并绑定 `extractive_control` 具体整句摘录可见文本。
- 区域2：绑定 `TOPIC_01_full/round_1/round_2` 三份公共无标签证据包的字节与规范哈希，`validate_packet(allow_demo=False)` 逐份重验，两轮拼回完整包，不含答案或量规。
- 区域3：公共问卷8锚题（4真4假，覆盖6维）＋4迁移题，私有金标准含12条整数0/1真值、6维评分细则与针对行动节奏轴的 `opposing_rubric`；100%通过 `measurement.validate_public_questionnaire` 与 `validate_private_gold_bundle`。`verify_topic01_pilot_materials` 重算整体哈希、重读源与证据、重验108卡、重跑96次排程、重建12份可见文本、重跑两个校验器并扫描三区零泄漏。
- `simulate_section52_dual_review` 覆盖§5.2八步：版本/ID/URL/时间/哈希；13条命题标 fact/value/prediction/definition/causal；`SIM_REVIEWER_A/B` 两个独立模拟槽；历史时间窗（拒绝把2011/2016/2025或页面修改日期混作2026观测统计）；英文翻译逐条对照 `mostly / it appears / until…limit / continues to absorb / based on models`；筛除规则与权利待办；难度与满分预案；冻结manifest及分歧门禁。默认在 `CL_E05` 演练分歧→`blocked_from_pass=True`→独立第三人 `SIM_ADJUDICATOR_C` 裁决闭环。
- 诚实门禁：输出恒含 `is_simulation_rehearsal=True`、`review_mode="simulated_rehearsal_not_human"`、`human_reviews_completed=0`、`approved_for_experiment=False`、`formal_eligible=False`、`subject_delivered=False`；明确只验证审核数据结构与裁决门禁，不替代真人签字。`cross_topic_20261108/human_review_checklist.json` 55项110位仍全部pending且字节未变。
- 22项专项测试通过；末次全项目 [validation_20261109T121218_e458e1.json](experiment/review/validation_20261109T121218_e458e1.json) 为 **793项、0 failures、0 errors、0 skipped、success=true**。独立汇报：[REPORT_step33_20261109.md](experiment/review/pilot_materials_20261109/REPORT_step33_20261109.md)。
- 已登记偏差：R2编辑组织稿232字符超出 `extractive_control` 可行区间141–214（R1为143–234），`editorial_within_extractive_feasible_range=False` 与 `deviation` 如实保留，未截断、未补字、未放宽10%。材料仍为离线候选，`is_demo=False` 只表示基于真实来源，不代表人工批准。

### 步骤34｜2026-11-09：三议题并行标准化材料包与统一门限校验

- 扩展 `cocoon/pilot_materials.py`：把步骤33硬编码的TOPIC_01逻辑参数化为 `_TOPIC_SPECS` 三议题冻结配置，新增 `build_topic_pilot_materials`、`build_all_topics_pilot_materials`、`verify_topic_pilot_materials`、`simulate_all_topics_dual_review` 四个公共API；旧三API保留为薄包装，`__all__` 扩为7个。纯标准库离线，只读 `intake/` 与既有build目录，不写正式材料文件。新增模型/API/网络调用0、费用0。
- 三议题差异素材全部取自各自 `intake/*/topic_material.json` 的六条证据与 `boundary_note`：能源5个真源（含IRENA一手页403失败后的二手转引、81%按新增容量且不采用）、天气4个中文真源（取证日2026-11-08非发布日、不从URL年月推断、WE_S05的HTTPS降级失败记录保留）。三份intake字节哈希与build manifest中 `source_material_sha256` 逐项一致，构建入口强制校验；`protocol_sha256=3d3ba6f0…6253`。
- `build_all_topics_pilot_materials` 用3线程池并行构建与校验，输出按TOPIC_01/02/03固定顺序；`parallel=False` 顺序模式结果逐字节一致（整体哈希含 `execution_mode` 审计字段）。统一 `pilot_manifest` 含 `build_id`、每议题 `build_id`、`protocol_sha256`、intake哈希与统一门限。三议题各72曝光＋36保持卡（180–220字符）、6分层、96次四环境排程100%可解、12冻结讨论槽、12份六臂两轮600–800剂量包（实测TOPIC_01 600–693、TOPIC_02 630–727、TOPIC_03 667–796）、8锚题4真4假＋4迁移题与6维私有金标准，全部通过 `measurement` 两个严格校验器。
- `verify_topic_pilot_materials(bundle, topic_id)` 新增四道统一门限：A每个真源权利预警完整且 `license_note` 逐字一致、intake哈希绑定；B `statement_dimension_map` 精确覆盖12题、8锚题绑定且6维全覆盖；C六臂两轮12份全部绑定 `extractive_control` 摘录对照（I0–I3附加文字须逐段是原证据整句＋引用，不新增事实或连接语）；D三区零泄漏、三区哈希互异、议题ID错配拒绝。
- `simulate_all_topics_dual_review` 并行执行三议题§5.2八步模拟，汇总 `disagreement_items_total=3`、`adjudicated_items_total=3`、`blocked_before_adjudication_total=3`（分歧条目 `CL_E05`/`EN_E05`/`WE_E05`），`all_topics_honest_gate_enforced=True`；三议题均演练分歧拦截→独立第三人裁决闭环，`human_reviews_completed=0`、`approved_for_experiment=False`、`formal_eligible=False` 强制生效。差异化审核：能源step4含二手转引/81%口径，天气为 `chinese_original_paraphrase_fidelity`（无虚构英文翻译环节）。
- 修复的真实校验缺口：`statement_dimension_map` 删除一条迁移题映射旧门限未拦截（已补12题精确覆盖）；步骤33仅I4/I5有摘录绑定（已扩至六臂12份）；权利预警原先只有布尔位（已升为bundle一级逐源列表并传入step1/step6）。TOPIC_01输出扩展标准化字段，旧22项测试除 `__all__` 集合断言同步更新外继续通过。
- 37项专项测试通过；首次回归 `validation_20261109T124652_6640e0.json` 因本轮在回归运行期间短暂把裸占位符写入core.json，出现6处JSONDecodeError（操作时序失误，非代码缺陷，失败记录保留）；恢复合法配置并单独复验读配置模块后原样重跑，末次全项目 [validation_20261109T130342_7a6f52.json](experiment/review/validation_20261109T130342_7a6f52.json) 为 **808项、0 failures、0 errors、0 skipped、success=true**。独立汇报：[REPORT_step34_20261109.md](experiment/review/pilot_materials_20261109/REPORT_step34_20261109.md)。步骤28–33受保护原件、账本、原方案及 `REPORT_step33_20261109.md` 字节未变；空白人审模板55项110位仍全pending。
- 已登记边界：三议题真源数按实际为4/5/4，不强行统一；步骤33的TOPIC_01 R2长度偏差仍保留；「并行」为确定性线程池并行、无共享写入。所有材料仍是离线候选，无一次真实送达。

### 步骤35｜2026-11-10：三议题全链路离线系统压力预演（工程合龙）

- 目的：按方案§6–11、§13.4、§15.1，把步骤34的三议题 Pilot 材料包、`scheduling`/`runtime` 分支与快照、步骤30/31的公共问卷·私有金标准·T1常规发言·双盲registry回填、步骤32的网络级2×2与槽位随机化检验串成一次端到端离线工程演练；**不修改** `engineering.dry_run` 的旧 SYNTHETIC 夹具行为。
- 新建 `cocoon/system_rehearsal.py`：两个公共API `run_pilot_system_rehearsal(evidence_root, *, blocks_per_topic=2, agents_per_world=8, seed=20261109, bootstrap_reps=200, permutation_reps=200)` 与 `verify_pilot_system_rehearsal(rehearsal_result)`。纯标准库、只读既有build目录、不落盘、不联网、不调用模型。冻结证据包按 bundle 内 `byte_sha256`/`canonical_sha256` 逐项复核后才用于 mirror 契约。
- 阶段1：三议题三区隔离材料包加载并各自重跑 `verify_topic_pilot_materials`，本模块另独立重扫零金标准/标签泄漏；合计216曝光卡＋108保持卡＋36冻结讨论槽＋36份六臂两轮干预包（600–796字符）＋3套公共问卷与私有金标准。冻结问卷/金标准/公共卡仅建立 `is_demo=True` 的演练深拷贝，内容逐字不变，原件字节未动。
- 阶段2：3议题×2区组×8人，A/B/C/D四世界共享人口/网络/初始状态核心哈希；8轮严格曝光共1536条 `exposure_delivered` 事件与1536条常规发言条目，`metrics.exposure_metrics` 实测 A/B `X=33.3333`、`Hn=1.0`，C/D `X=16.6667`、`Hn=0.7897`，A/C错误卡比例0、B/D 1/3，最大单卡重复≤2。T0/T1逐受试测量上下文＋12次完整状态排除审计；T1从常规发言提 `user_view` 并驱动192次 `parse_stage_output(..., "mirror", ...)` 严格通过。
- 阶段3：每区组 `scheduling.allocate` 生成六臂槽位，克隆36个隔离分支；处理前核心哈希与父T1快照100%一致、父快照投递后不变、identity互异且隔离探针通过。六臂两轮共576次合规可见文本投递（补齐旧 `dry_run` 中 `I0–I3` 的 `visible_text=None` 缺口，旧源码与行为未改）；T2测量后4轮独立保持卡池共1152次送达，再执行T3主终点测量。
- 阶段4：确定性合成器只依据已见 `visible_card_ids` 与预设条件标签生成附录B三字段回答与盲评，**从不读私有金标准、不模拟认知变化**；走完 `parse_subject_measurement_output` → `create_blind_sample_registry` → `parse_blind_evaluation_output` → `reconcile_blind_evaluations(expected_registry_sha256=...)`，1248/1248样本全量回填（零pending）。交 `analysis.aggregate_panel_to_networks(8, allow_demo=True)` 得156条有效网络记录，再跑 `analyze_exposure_2x2`（6区组全可估）与T2/T3两个终点 `analyze_intervention_effects(allocations=...)`，均输出 `p_raw` 与 `metrics.holm` 的 `p_adjusted`。
- `verify_pilot_system_rehearsal` 逐项独立复核§15.1：三区零泄漏、六臂非空600–800、父子处理前哈希一致、跨臂零可变状态共享、测量零记忆写回（1152次前后哈希一致）、全量面板回填与网络重算有效、12个诚实门禁位锁定；另重放192次mirror、重算整体 `integrity_sha256`、从存储面板独立重跑网络聚合/2×2/T2/T3统计并比对完整规范哈希。
- 36项专项测试通过，含第二次完整独立运行的端到端数值复现（`integrity_sha256=7a0aab1f…d31115` 与首次逐位一致）与10类篡改拦截；测试在 `socket.socket`/`socket.create_connection` 全面禁用下完成，且不向旧审阅或取证目录写入文件。末次全项目 [validation_20261110T090840_f63bab.json](experiment/review/validation_20261110T090840_f63bab.json) 为 **844项、0 failures、0 errors、0 skipped、success=true**。独立汇报：[REPORT_step35_20261109.md](experiment/review/pilot_materials_20261109/REPORT_step35_20261109.md)。
- 诚实门禁全程锁定：`rehearsal_mode="offline_system_stress_rehearsal"`、`is_demo=True`、`synthetic_rehearsal_response=True`、`actual_model_calls=0`、`human_reviews_completed=0`、`approved_for_experiment=False`、`formal_eligible=False`、`formal_launch_enabled=False`、`subject_delivered=False`；统计输出显式标 `statistical_outputs_are_synthetic=True`。新增模型/API/网络调用0、费用¥0；累计¥0.03430324、剩余¥4.96569676不变。
- 边界如实登记：规模为3×2×8的**压力预演**，不是§6.1的18区组×16人核心规模；常规发言、测量回答、盲评及全部p值/效应量都是确定性合成，只证明链路可运行可复现，不具实验推断意义；六臂T1复用父D快照输出是 `analysis._shared_baseline` 的契约要求；逐受试只读测量视图＋12次抽样式完整状态排除审计是为控制纯Python严格校验耗时，未放宽任何步骤30/31校验器；步骤28–34受保护原件、账本、原方案与空白人审模板字节SHA-256全部未变。

### 步骤36｜2026-11-11：方案A（AI双视角独立核验+第三人裁决+受控放行门禁）

- 目的：用户已拍板采用方案A，用两个不同审计重点的AI核验视角加一个独立第三人裁决视角，代替真人逐项手填55项/110个审核槽位；要求在不修改原空白模板与 `cocoon/human_review.py` 的前提下，直接通过步骤29 `merge_and_verify_human_reviews` 与 `verify_human_review_submission` 的严格核验，并提供受控的一键放行门禁。
- 新建 `cocoon/ai_assisted_review.py`：`build_scheme_a_review_copies` / `run_scheme_a_merge_and_verify` / `evaluate_ai_assisted_release_gate` 三个公共API。纯标准库、只读既有模板与取证构建、不联网、不调用模型、不写文件。新建 `scripts/export_scheme_a_snapshot.py` 与 `experiment/review/ai_assisted_review_20261110/scheme_a_merged_verified.json`（344,493字节）。
- 三份副本全部由权威空白模板深拷贝：`reviewer_1_copy` 只填 `MEMBER_B_SOURCE_VERIFIER` 列（55/55，全键True、带 `+08:00` 时区ISO时间、逐条实质意见引用具体 id/引文/来源/偏移区间），另一列与adjudication逐字节保持空白；`reviewer_2_copy` 只填 `MEMBER_C_CONTEXT_AUDITOR` 列（51项通过＋4项 `needs_revision` 各含1个False检查）。单列越权0。第三人副本逐字保留两份初审列，只填 `MEMBER_E_CHIEF_ADJUDICATOR` 的裁决。
- 4项真实初审分歧取自 `independent_review.json` 的优先关注点：`EV_CL_E05`（语境保留，同页碱性语境与pH方向定义段）、`EV_EN_E05`（语境保留，2023就业存量依赖同屏前句与二手转引）、`EV_WE_E01`（语境保留，百分比的产品范围与时段限定）、`EV_WE_E05`（数字日期否定模态，2020-05-12历史答复日期仅在同屏标签）。第三人完整核对同屏证据块与边界说明后给出通过型裁决、全键True checks与详实理由，不改写两位初审员原意见。
- 权威合并核验实测：`completed_human_slots=110`、`completed_items=55`、`dual_reviewed_items=55`、`disagreement_items=adjudicated_items=4`、`unresolved_disagreements=awaiting_adjudication_items=0`、`pending_items=0`、`needs_revision_items=0`、`rejected_items=0`、`passed_items=55`、`human_reviews_completed=2`、`content_review_passed=True`、`release_gates_passed=True`、`all_55_items_resolved=True`、`all_55_items_passed=True`；`status=lightweight_review_passed_not_formally_eligible`，`approved_for_experiment=False`、`formal_eligible=False`。`verify_human_review_submission` 二次复核与合并结果规范哈希一致（幂等）。
- `evaluate_ai_assisted_release_gate`：默认 `allow_ai_assisted_release=False` 时 `pilot_release_unlocked=False`；显式传 True 时 `pilot_release_unlocked=True`、`ai_assisted_approved_for_pilot=True`、`full_108_card_pilot_pack_verified=True`、`all_55_checklist_items_passed=True`、`release_scope=pilot_materials_only_ai_assisted_scheme_a_authorized_by_user`，同时恒有 `review_origin="ai_assisted_dual_perspective_scheme_a"`、`real_human_ca_signature_verified=False`、`formal_eligible=False`，`release_blockers` 仍保留 `real_human_review_not_completed` 与 `formal_experiment_eligibility_not_granted`。三议题材料实测216曝光卡＋108保持卡＋36讨论槽＋36干预包＋3问卷＋3私有金标准，三议题八步模拟全存在、3分歧全裁决、3诚实门禁全生效。
- 30项专项测试通过（覆盖三份副本、单列越权0、分歧触发与第三人裁决闭环、110槽/55项全通过、默认锁定vs一键解锁、7类篡改拦截、原件SHA保全、禁网）；测试在 `socket.socket`/`socket.create_connection` 全面禁用下完成，且不向既有审阅或取证目录写入文件。末次全项目 [validation_20261111T061740_93ade4.json](experiment/review/validation_20261111T061740_93ade4.json) 为 **874项、0 failures、0 errors、0 skipped、success=true**。独立汇报：[REPORT_step36_20261110.md](experiment/review/ai_assisted_review_20261110/REPORT_step36_20261110.md)。
- 诚实登记：`review_origin` 不写进合并件本身，因为 `human_review._review_shape` 严格限制顶层键；该标记记录在返回包、放行包与落盘快照中。`human_reviews_completed=2` 是「角色列数」不是两名已认证真人；`identity_verified=False`；7项发布门禁的通过是方案A代理结论，不构成真人身份认证、电子签名或法律意见，`formal_eligible` 恒为False。原空白模板 SHA-256 `fd2d9adde69f4785…0706` 未变、仍 `pending_human_review`；`cocoon/human_review.py` 与步骤28–35全部受保护原件字节未变。新增模型/API/网络调用0、费用¥0；累计¥0.03430324、剩余¥4.96569676不变。

### 步骤37｜2026-11-11：三议题全链路可视化看板与离线结案交付包

- 目的：按方案§12.1–12.4与§16，把步骤34材料包、步骤35系统压力预演与步骤36方案A签发导出为可复核的派生数据包、单文件自包含只读看板与§12.4验收，并产出离线结案ZIP归档。
- 新建 `cocoon/dashboard.py`：`build_dashboard_dataset` / `render_experiment_dashboard` / `verify_dashboard_bundle` 三个公共API；新建 `tests/test_dashboard.py`（28项）与 `scripts/export_closeout_archive.py`。纯标准库、只读既有产物、不联网、不调用模型。
- 数据包实现：调用 `pilot_materials.build_all_topics_pilot_materials`、`ai_assisted_review.run_scheme_a_merge_and_verify` 与 `evaluate_ai_assisted_release_gate`、`system_rehearsal.run_pilot_system_rehearsal` 与 `verify_pilot_system_rehearsal`；另解析计费账本（10次结算、¥0.03430324、余额¥4.96569676）、8次测试里程碑与3项短投递失败（`length_out_of_range`×2、`invalid_schema`）。
- **逐样本重建**：预演面板只存哈希与分数，故用固定seed的 `scheduling.schedule_cards` 重建1248条样本的可见卡与合成回答；与面板对账结果——样本数1248/1248、`BLIND_%04d` 置换与七元组0处不一致、回答规范哈希1248/1248一致、U三分项1248/1248一致。因此看板每个点可按§12.4回溯到网络→个体→题目/证据→原始来源哈希。
- 11个视图全部落地：①实验总览（矩阵/方案A 110槽/账本/失败留痕/里程碑）；②同步时间轴（T0→8轮→T1→四环境快照→六臂分支→2轮干预→T2→4轮保持→T3，含逻辑序号与哈希）；③网络回放（6个8人固定坐标SVG，同立场16/异立场16条边）；④信息流对照（A/B X=33.33、C/D X=16.67，Hn=1.0/0.7897，错误卡0/0.333，配额与每轮6卡）；⑤个体轨迹（480条、S>0红点、三类案例）；⑥六臂对照（36份600–796字符、I4/I5共同证据块与附加段匹配）；⑦证据追踪（25条可展开链）；⑧群体结果（2×2三效应+六臂配对+SVG森林图）；⑨置信度校准（3区间×正误，锚题8/迁移4分母分离，anchor_n=9984、transfer_n=4992）；⑩六维覆盖与U（掌握+缺口+遗漏=100，复述/论据/边界三分项，U分布）；⑪系统质量与治理（引用契约192/192、4争议裁决、逐源权利预警、§15.1门禁）。
- §12.3三类案例（固定seed确定性规则）：改善 `TOPIC_02/B01/I4/S01` ΔBS=−0.3317；无变化 `TOPIC_01/B02/I4/S06` ΔBS=+0.0138（|ΔBS|最小但非恰为0，已如实标注）；反向 `TOPIC_02/B02/I4/S05` ΔBS=+0.2939。每条含 `(topic,block,world,arm,agent,item,card)` 追溯键。
- 页面与验收：横幅持续固定并含指定文本；6个全局筛选器联动11个 `live-*` 区域；响应式与打印样式；去数据块后 `script src`/`link href`/`@import`/`url(http`/`fetch(`/`XMLHttpRequest`/`iframe`/`http(s)://` 均为0，凭据模式均为0。`verify_dashboard_bundle` 输出25条路径、130个节点逐节点重放，156条网络均值由1248面板重算一致，6区组2×2由 `metrics.exposure_contrasts` 重算一致，T2/T3 `p_adjusted` 由 `metrics.holm` 重算一致，方案A汇总重跑一致。
- 产物：`experiment/dashboard_20261110/dashboard.html`（1,364,824字节）、`dashboard_data.json`（1,524,829字节，`dataset_sha256=c28bf300…3c3c9f`）、`verification.json`、`REPORT_step37_20261110.md`；`experiment/exports/cocoon_closeout_dashboard_20261110.zip` 白名单收录看板三件、方案A签发快照、步骤28审阅页、步骤28–37共9份Markdown汇报与PROGRESS索引，并附 `MANIFEST.md`/`MANIFEST.json`（逐文件SHA-256），归档时强制排除 `intake/`、`.source.json` 与凭据。
- 28项专项测试通过，含11视图存在性、25条全链追溯、横幅强制展示、无外链/凭据、6类篡改拦截与原件SHA保全；测试在 `socket.socket`/`socket.create_connection` 全面禁用下完成，且不向既有审阅或取证目录写入文件。末次全项目 [validation_20261111T084340_5e169a.json](experiment/review/validation_20261111T084340_5e169a.json) 为 **902项、0 failures、0 errors、0 skipped、success=true**。独立汇报：[REPORT_step37_20261110.md](experiment/dashboard_20261110/REPORT_step37_20261110.md)。
- 诚实登记：看板展示的是预演数据而非实验结果；方案A为代理签发、`real_human_ca_signature_verified=False`、`formal_eligible=False`；规模为3议题×2区组×8人的压力预演，不是§6.1核心规模；三类案例按固定规则遴选、不挑“最漂亮轨迹”；个体轨迹只有四时点、不插造逐轮测量；来源URL仅作纯文本不发起请求。步骤28–36受保护原件、账本、原方案与空白人审模板字节SHA-256全部未变；新增模型/API/网络调用0、费用¥0。

### 步骤38｜2026-11-11：修复看板 UI 排版缺陷并统一 11 视图排版

- 缺陷（用户实机发现）：`view-02` 时间轴每个阶段胶囊 `.chip` 从中间断裂成左右两个半圆弧，且未横向排列而逐行竖向堆叠。
- 根因：①旧 `_CSS` 的 `.chip` 未声明任何盒模型，默认 `display:inline`，而其子元素 `.chip small{display:block}` 为块级；行内盒不得包含块级盒，浏览器触发 **inline-box splitting**（行内盒拆裂），`border-radius:999px` 的边框因此在中间断开、`<small>` 各自换行；②旧 `_JS` 的 `renderTimeline()` 把胶囊直接拼进 `<p>` 文本流，未使用静态区已有的 `.chips` 弹性容器。
- 修复：`.chip` 改为 `display:inline-flex;flex-direction:column;align-items:flex-start;justify-content:center;vertical-align:middle;border-radius:10px;padding:5px 10px;line-height:1.3` 并加 3px 相位色条；静态 `view-02` 与动态 `live-02` 统一为 `.timeline`→`.timeline-row`（`158px minmax(0,1fr)` 两列）→`.timeline-head`＋`.chips`，同区组 23 个阶段胶囊横向流式排列、`≤760px` 转单列自动折行，胶囊自身不再断裂。
- 全视图巡检与升级：`_table()` 统一外包 `.table-wrap`（`overflow-x:auto`、内表 `min-width:520px`），`th,td` 加 `overflow-wrap:anywhere`；新增 JS `tblWrap()` 覆盖 `renderSeries/renderInterventions/renderTrace/renderFlow/renderCalibration/renderCoverage/renderNetwork`，`.live` 亦加 `overflow-x:auto`；`view-03` 改为 `.net-grid{repeat(auto-fit,minmax(240px,1fr))}`（`≥1100px` 3列、`≤900px` 降列）的 6 张 `.net-card`，并把会重复绘制 6 张 SVG 的 `renderNetwork()` 改为紧凑筛选表；`.banner` 与 `.filters` 合并进唯一 sticky 容器 `.topbar{position:sticky;top:0}`，删除 `.filters` 自身的 sticky 与硬编码 `top:56px`，横幅折行不再遮挡筛选器；全页 `<span>` 内含 `<small>`/块级子元素的残留冲突数 0（仅 `.chip` 与 `.banner div` 两处合法）。
- 自动防回归：`verify_dashboard_bundle` 新增 `_ui_layout_audit` 九项硬断言（胶囊盒模型与 `flex-direction`、静态 `timeline-row`+`chips`、`renderTimeline()` 函数体结构、`.table-wrap` 滚动、JS `tblWrap`、`.net-grid`+6 卡、`renderNetwork()` 内不得有 `<svg>`、单一 sticky 顶栏且无 `top:56px`、全页行内块冲突扫描），`verification.json` 新增 `ui_layout` 段。
- 实测（本机 Edge 无头真实排版，1440/900/430px）：`.timeline-row` 12 个（静态6+动态6）、计算样式 `display:flex;flex-direction:column;radius:10px`、超出卡片右边缘的胶囊数 **0（maxOver=0px）**、`.net-card` 1440px 下 3 列×437px、430px 下 2 列×210px、三断点 `scrollWidth==clientWidth`（1418/1418、478/478）无页面级横向溢出；内联 JS 通过 `node --check` 并在假 DOM 下执行出 6 行时间轴/138 胶囊/6 拓扑卡。
- 产物：`dashboard.html` 1,369,935字节（原1,364,824）、`verification.json` 2,068字节（新增 `ui_layout`）、`dashboard_data.json` 1,524,829字节（重建后仅 `generated_at_utc` 与 `overview.milestones` 两处差异，其余24个顶层键逐字节相同，`dataset_sha256=af49d724…c769f`，证明只改表现层未动任何派生数值）；结案ZIP已重建并纳入本报告（SHA-256 见 `.sha256` 侧车）。
- 专项测试：`tests/test_dashboard.py` **37项全部通过**（原28项＋新增9项：胶囊盒模型、静态/动态时间轴容器、宽表滚动包装、网格与单一 sticky 顶栏、审计器自证、3类UI篡改拦截）。末次全项目 `python -m cocoon validate` 为 **911项、0 failures / 0 errors / 0 skipped、success=true**（`experiment/review/validation_20261111T092930_d6cef2.json`）。
- 诚实登记：本次仅表现层修复，不改任何派生数值/案例/效应/p值；未做跨浏览器全矩阵认证（Firefox/Safari/真机未逐一实测），所用 flex/grid/sticky 均为基线特性；步骤28–37受保护原件、账本、原方案与空白人审模板字节SHA-256全部未变；新增模型/API/网络调用0、费用¥0。

### 步骤39｜2026-11-11：剩余五轮真实组织侧生成与六轮整句摘录配对合龙

- 目的：用户授权真实调用；把 `TOPIC_01_R2`、`TOPIC_02_R1`、`TOPIC_02_R2`、`TOPIC_03_R1`、`TOPIC_03_R2` 五轮的组织侧（I4 候选）由编辑稿升级为真实 `mimo-v2.6-flash` 输出，并与确定性整句摘录（I5）完成结构配对，形成 6/6 全量清单。
- 新建 `cocoon/live_cross_topic_delivery.py`：`run_remaining_live_organized_deliveries`（`execute=True` 且凭据/账本/配置就绪才发请求）、`build_six_round_live_extractive_manifest`、`verify_six_round_live_extractive_manifest`、`summarize_live_delivery`、`live_pairs_for_materials`；新建 `tests/test_live_cross_topic_delivery.py`（27 项）。
- 生成：模型标识 `mimo-v2.6-flash`、`temperature=0`、`thinking=disabled`、`max_tokens=1024`；只发送冻结证据包、四句预算与硬边界，不发送内部报告。首轮三/五轮因总长或单句越界被本地拒绝后，重试请求携带**上一轮实测句长**与硬边界反馈（system 提示词未改），每轮最多 3 次；全部尝试均写入 EventStore 与账本。
- 结果：六轮组织侧 175/166/223/188/176/207 字符，全部落在各轮可行区间；可见总长 I4/I5 = 632/637、625/619、715/726、663/671、689/673、764/764，最大相对差 2.377%；七项检查逐轮全通过。`TOPIC_01_R2` 232 字符偏差消除（`deviation=None`）。
- 清单：`experiment/review/live_cross_topic_20261111/six_round_live_extractive_pairs.json`（34 289 字节，`manifest_sha256=7ce6fd83…5e882c`），逐轮含 Run ID、尝试次数、Token、账本费用、I4/I5 文本 SHA-256、七项检查与 `prompt_variant`。
- 记账：连通性冒烟 ¥0.000057 + 六轮最终运行 ¥0.01765808 + 被替代/中断尝试 ¥0.00385868 = **¥0.02157376**；账本 23→59 行，累计 ¥0.03430324 → **¥0.05587700**，剩余 **¥4.94412300**，`reconciled=true`，无删除或改写任何一次尝试。
- 接入：`pilot_materials` 六臂包 I4 改用真实输出（`content_origin=live_model_organized_output`）、I5 用确定性摘录，单议题入口默认 `live_pairs="auto"`；看板 `view-01`/`view-06`/`view-11` 展示 6/6 状态、Run ID、Token、费用、治理与重合登记；`verify_dashboard_bundle` 新增 `live_delivery` 重算校验。
- 披露：①R1 有父级内部报告、其余五轮纯证据包，`prompt_variant` 逐轮标注，不可当完全同条件重复；②3 处 I5 与中性臂文本重合（T01/R1↔I0、T02/R2↔I2、T03/R1↔I2）已登记 `dose_arm_collisions`，12 包实际不同附加文本为 9 份，待真人审决定；③一次主控中断的真实尝试（¥0.002141）已归档 `live_deliveries/_aborted/` 并写入 `aborted.json`；④`subject_delivered=false`、`human_reviews_completed=0`、`full_I4_eligible=false`、`formal_eligible=false`、`approved_for_experiment=false`，语义质量未评。
- 验证：`tests/test_live_cross_topic_delivery.py` 27 项通过；受影响的 `test_pilot_materials`/`test_dashboard`/`test_system_rehearsal`/`test_ai_assisted_review` 共 140 项按新事实更新后全通过；全项目 `python -m cocoon validate` 为 **938 项、0 failures / 0 errors / 0 skipped、success=true**（`experiment/review/validation_20261111T132036_0447bf.json`）。独立汇报：[REPORT_step39_20261111.md](experiment/review/live_cross_topic_20261111/REPORT_step39_20261111.md)。

### 步骤40｜2026-11-13：TOPIC_01 真实 mimo-v2.6-flash 端到端微型实证预演

- 目的：用户授权真实调用；在环境 D（同质 + 含误导）下让 `mimo-v2.6-flash` 扮演 S01（+1）与 S05（−1），走完 T0 → 8 轮曝光（每人 48 卡次）→ T1 常规发言 + T1 测量 + 真实 Stage 5 mirror → 父快照克隆 6 分支（I0/I5/I4）→ 2 轮干预 + 单次回应 → T2 → 4 轮保持 → T3 → 16 份真实盲评 → 面板回填。
- 新建 `cocoon/live_micro_pilot.py`（`run_topic01_live_micro_pilot`、`build_topic01_live_micro_pilot_manifest`、`verify_topic01_live_micro_pilot`、`summarize_live_micro_pilot`）与 `tests/test_live_micro_pilot.py`（28 项：9 离线契约 + 19 真实清单重放/篡改）。
- 工程适配（用户批准）：B02 区组、48 卡次、R1 的 I0/I5 文本相同如实披露、单条转录确定性展开、先跑 4 阶段再逐受试 mirror（mirror 不送分支）。
- 运行：4 次真实运行全部留痕——①`…064017Z` T1 发言三次超长/含字母失败（5 次，¥0.01269312）；②`…064439Z` 外层 600 秒超时 SIGTERM 中断（23 次结算 + 1 次在途，¥0.15045424）；③`…070337Z` S05 T1 测量三次输出发言而非 JSON（18 次，¥0.07723428）；④**`…071307Z` 完成（52 次，0 被拒，¥0.18835572）**。①③后分别修订提示词为明确目标字数、测量格式提醒与可执行反馈（v3），未改问卷/材料/校验器/评分。
- 结果：16/16 测量与 16/16 盲评全回填；两名受试 T0 即 Acc=100、S=0、U=100、BS 0.0072，T1 BS 0.0034，T3 BS：S01 I0/I5/I4 = 0.0034/0.0044/0.0044，S05 = 0.0025/0.0034/0.0034；O 在 0–50 间离散跳动，属单样本盲评粒度噪声。**结论：天花板效应，该模型对本议题锚题天然免疫，三臂无可区分效应；不是破茧助手有效或无效的证据。**
- 记账：本步 98 次已结算 + 1 次在途、输入 628 128 / 输出 62 185 tok、**¥0.42873736**；账本 59→257 行，已结算累计 ¥0.05587700 → **¥0.48461436**；在途请求 `…091886789:respond_S01_I4_R1:1` 登记 `uncertain/interrupted`，按最坏情况 ¥1.050624 持有（`available_cny=3.46476164`、`needs_reconciliation=true`），未伪造结算。
- 门禁变更（用户授权）：`cocoon/budget.py` 新增 `HELD_INTERRUPTED_REQUEST_IDS`（仅上述 1 个 ID），该请求处于 `uncertain+interrupted` 时不再阻塞新预留；`mimo_probe.mimo_status` 扣除持有数；`live_micro_pilot` 改用 `charged_cny` 计费差。新增 `HeldInterruptedTests` 3 项。
- 看板：`view-01/05/07/10` 新增“真实 mimo-v2.6-flash 微型实证对照”区块（与 1248 样本预演分开）；`verify_dashboard_bundle` 新增 9b 重验；`test_dashboard` 新增 2 项。看板三件与结案 ZIP 已重建。
- 回归留痕：前两次全量回归未通过并原样保留（`validation_20261113T080902_ad1650`：回归中改写 core.json + 持有预留使 `total_cost_cny=null` 致 `render_live_review` 崩溃；`validation_20261113T084011_971675`：误改 `reporting.py` 字节冻结前段）。已还原 `reporting.py`，改在 `live_audit.py` 保留原始 null 并给出“已结算＋待对账”展示值，`live_cross_topic_delivery` 计费差改用 `charged_cny`。
- 验证：全项目 `python -m cocoon validate` 为 **971 项、0 failures / 0 errors / 0 skipped**（`experiment/review/validation_20261113T090943_aee325.json`）；步骤28–39 受保护原件与空白人审模板字节不变；凭据只经环境变量，产物扫描 0 命中。独立汇报：[REPORT_step40_20261111.md](experiment/review/live_micro_pilot_20261111/REPORT_step40_20261111.md)。

### 步骤41｜2026-11-13/14：账本受控提额 + 三议题真实端到端认知实证矩阵合龙

- 提额：`cocoon/budget.py` 新增 `raise_limit` 事件（字段 `previous_limit_cny/new_limit_cny/reason`）与 `BudgetLedger.raise_limit()`；回放校验 previous 等于当前有效上限、新上限严格增大、原因为小写短码、封禁时拒绝；构造函数仍绑定 init 原始额度。共享账本追加第 258 行 ¥5.00→¥50.00（`step41_group_showcase_three_topic_live_expansion`），原 257 行逐字节保留。`test_budget` 由 43 项增至 48 项。
- 议题参数化：`live_micro_pilot.topic_spec()` 统一议题规格（B02 区组种子 `BASE_SEED + topic_index*10007 + 101`）；`load_materials / run / build / verify / summarize` 支持任意议题并保留 `*_topic01_*` 兼容入口；`_superseded_runs` 按议题前缀过滤。TOPIC_01 清单（`166aea62…29dc0`）与运行目录字节未改，重放核验仍通过。
- 受试规则（用户选定）：S01 + 从 S05 起首个与 S01 立场相反者 → TOPIC_01 S01(+1)/S05(−1)，TOPIC_02 S01(−1)/S07(+1)，TOPIC_03 S01(+1)/S07(−1)。议题名以冻结证据包为准：TOPIC_02 能源转型、TOPIC_03 天气信息核查（任务书写作电动车/超加工食品，有误）。
- 真实运行（两条独立后台命令）：TOPIC_02 首次 `…T153611Z_dec2ac35` 在 `mirror_S01_T1` 三次被拒（JSON 前复述契约；`user_quote` 截断原句自补“。”），11 次调用 ¥0.07247108，已写 `aborted.json`；新增 mirror 逐条引句诊断与可执行反馈（`FEEDBACK_REVISION=micro_pilot_feedback_v4_mirror_quote_diagnostics`）后重跑 `…T154342Z_c8b02e48` 完成（53 次，1 次被拒重试，¥0.26189364）；TOPIC_03 `…T160101Z_12c93e3f` 完成（57 次：1 次 mirror 被拒重试 + 四阶段首任务未过校验后重做 4 次，¥0.31921652）。
- 矩阵：`build_three_topic_live_micro_pilot_matrix` / `verify_three_topic_live_micro_pilot_matrix` / `summarize_three_topic_matrix`；`three_topic_live_micro_pilot_matrix.json`（`matrix_sha256=6a135322…ccba1`）汇总 3 议题 × 2 受试 × 3 臂 = 18 分支，采纳 156 / 实际 162 次调用，48 面板行（72 行四时点展开），48 测量 + 48 盲评，6 mirror，36 回应，9 行议题×臂描述性对比与逐运行账本对账。
- 结果：三议题均 T0 即 Acc=100、S=0；三臂 T3 BS：TOPIC_01 0.0030/0.0039/0.0039，TOPIC_02 0.0034 ×3，TOPIC_03 0.0025 ×3；无可区分臂效应。曝光阶段描述性变化：TOPIC_03 BS 0.0216→0.0030、U 58.3→91.7（T3 100）；TOPIC_02 U 75→100。
- 看板：view-01 矩阵 KPI 与运行清单；view-05 跨议题描述性表 + 3 张 SVG 四时点轨迹 + TOPIC_02/03 发言/mirror/回应原文；view-07 TOPIC_02/03 节点追溯；view-10 三议题 T3 O/U 与异见原文；`verify_dashboard_bundle` 新增 9c 重算；计费摘要改取最后一次 `raise_limit`（¥50.00）并列出持有预留与扣持有后可用额。
- 记账：本步 121 次结算、输入 762 039 / 输出 76 166 tok、**¥0.65358124**；账本 257→500 行，已结算累计 ¥0.48461436 → **¥1.13819560**；扣持有后可用 ¥47.81118040；仍仅 1 条步骤40 中断持有预留。
- 验证：全项目 `python -m cocoon validate` 为 **992 项、0 failures / 0 errors / 0 skipped**（`experiment/review/validation_20261113T170455_6c3e4d.json`）。独立汇报：[REPORT_step41_20261113.md](experiment/review/live_micro_pilot_20261111/REPORT_step41_20261113.md)。

### 步骤42｜2026-11-14：§5.4 封闭去先验情境真实实证 + 答辩路演看板 + 总结案白皮书与五人答辩攻略

- 目的：步骤41 证实三议题存在 T0 即 Acc=100 的先验天花板；按方案 §5.4 构建封闭虚构情境，用真实 `mimo-v2.6-flash` 检验去先验后的茧房形成与 I0/I5/I4 纠偏；升级看板为答辩路演版；交付总结案报告与五人答辩攻略。
- 新建 `cocoon/closed_world_pilot.py`：确定性材料（`materials_sha256=63500cce…59cb1`，来源为 `https://*.xinglan.synthetic.invalid/`，误导卡仅为网帖口径）、可配长窗口枚举（R1 143–248、R2 127–239 字）、I4 组织段（v3 逐轮单独调用，输入为 T1 发言 + mirror + 四阶段 + 本轮证据块，不含问卷/金标准/六维清单）、I5 `select_exact_sentences` 配长与七项检查、四阶段复用 `load_four_stage_source`、运行/清单/核验/摘要；新建 `tests/test_closed_world_pilot.py`（31 项）。
- 真实运行（5 次，全部 `aborted.json`/清单留痕）：①`…041348Z_6b4a4043` 组织段超窗（16 次，¥0.08006312）；②`…042318Z_3a69aa08` 四阶段 blindspot 复述契约 ×3（14 次，¥0.04717904）；③`…043249Z_fa670af9` 第 5/16 盲评上游 HTTP 500（41 次，¥0.12473804，1 条 `uncertain/http_error` 持有 ¥1.052672）；④`…052006Z_5eeb5a4f` S02 组织段缺问句/JSON 未闭合（10 次，¥0.02328684）；⑤**`…052738Z_8ac5d3e9` 完成（55 次，¥0.16829176）**。
- 门禁变更（用户授权）：`budget.HELD_HTTP_ERROR_REQUEST_IDS` 仅 `closed_world_synth01_20261114T043249Z_fa670af9:blind_BLIND_0005:1`，须处于 `uncertain+http_error`；新增 `HeldHttpErrorTests` 3 项。
- 结果：见上方第 1 节摘要；逐题与原文见 `REPORT_step42_20261114.md` §4。待人工复核：S02 I4 R1 一句引用错位（XL_E06 事实标为 XL_E03）、I5 迁移题 Q09 理由与概率矛盾、I0 两轮回应逐字相同。
- 看板：顶栏 7 步聚光灯导览（上一步/下一步/直达、←/→ 键、聚光框）+ 固定提词卡 + 静态 7 步提词全文；view-01 双轨对比专区（并排大表 + 5 指标双格 SVG，同轴）；view-05 合成情境逐题概率、T1 发言、mirror、I4/I5 并排、三臂回应；view-07 节点追溯；`verify_dashboard_bundle` 新增 9d/9e（提词卡结论句按数据自动分支并逐字重算）。看板三件重建（`dataset_sha256=fc2ffd9b…9cd3`），结案 ZIP 重建并收录封闭情境清单、总结案报告与答辩攻略。
- 记账：本步 136 次 HTTP、已结算 **¥0.44355880**；账本 500→772 行，已结算累计 ¥1.13819560 → **¥1.58175440**；持有 2 条合计 ¥2.103296，可用 ¥46.31494960。
- 验证：全项目 `python -m cocoon validate` 为 **1031 项、0 failures / 0 errors / 0 skipped**（`experiment/review/validation_20261114T063037_ac1280.json`）。一次 `test_dashboard` 在真实运行写账本期间执行，受保护账本变化导致 1 失败 + 1 错误，属预期并发假阳性，已由全量回归复核。独立汇报：[REPORT_step42_20261114.md](experiment/review/live_micro_pilot_20261111/REPORT_step42_20261114.md)；总结案：[FINAL_PROJECT_REPORT_20261114.md](experiment/review/FINAL_PROJECT_REPORT_20261114.md)；答辩攻略：[DEFENSE_PRESENTATION_GUIDE_20261114.md](experiment/review/DEFENSE_PRESENTATION_GUIDE_20261114.md)。

### 步骤43｜2026-11-15 12:00–13:20：5 分钟答辩演示页 v2（一屏一图动态交互沙盘）+ 反 AI 味硬门禁正式入档
- 目的：接管此前未走标准流程、未入档的 5 分钟演示页初稿 `five_minute_showcase_v1`（满屏 Emoji、渐变字、胶囊堆砌、底部常驻提词器、第 2–4 幕文字墙），重构为投影用的一屏一图动态沙盘，并把“反 AI 味”规范写进自动化门禁，完成全量回归入档。
- 实际操作：重写 `cocoon/showcase.py`，保留导出符号 `SHOWCASE_CONTRACT`/`build_showcase_payload`/`render_five_minute_showcase`/`verify_five_minute_showcase`。数据层：核查旁注改为冻结证据原文；沙盘气泡只用原话逐字子串（发帖 3 条/受试，回应 ≤24 字/轨）；逐受试 T3 指标；S02 R1 错位旗标由原文句子校验；去掉“飙升”“暴降 99%”等夸大文案。表现层：四幕由 Python 确定性生成 SVG，即 `clone-stage`/`dye-stage`/`track-stage`/`final-stage`；纸感点阵视觉，语义色只用朱砂红/青黛/琥珀，辅以墨绿/石板灰；48px 单行顶栏含进度节点、05:00 计时与抽屉按钮；左下角诚实角标；四 Tab 侧滑抽屉在服务端预渲染、默认关闭；提词器默认隐藏（T）；快捷键 1–4、←/→（抽屉打开时锁定）、Space、T、D、Esc。核验：新增 `_ui_sandbox_audit` 与 `_payload_truth_audit`，置于整页逐字节比对之前；`VALIDATION_PATH` 仍固定为 `validation_20261114T063037_ac1280.json`。新写讲稿 `FIVE_MINUTE_SHOWCASE_SCRIPT_20261115.md`，含五人接力（A/B/C/E/D）逐秒操作、抽屉追问用法与禁用说法表；旧讲稿 `…20261114.md` 保留不改。
- 输入版本/文件：`dashboard_data.json`（`dataset_sha256=fc2ffd9b…9cd3`）、`closed_world_synth01_live_pilot.json`、`closed_world_pilot.build_closed_world_materials()`、归档验证报告 `validation_20261114T063037_ac1280.json`，均只读。被替换的 v1 SHA-256：`showcase.py` `6cec04ab…f1`，`test_showcase.py` `84edff04…5d`，`showcase_5min.html` `f880a71d…bb`。
- 新增或修改文件：`cocoon/showcase.py`（`f7e42080…1e81a`）；`tests/test_showcase.py`（19 项，`822db8df…82be6`）；`experiment/dashboard_20261110/showcase_5min.html`（306 505 字节，`924fd359…c009`，`showcase_sha256=8f682f8b…afc2`）；`experiment/review/FIVE_MINUTE_SHOWCASE_SCRIPT_20261115.md`；`experiment/review/REPORT_step43_20261115.md`；`experiment/review/validation_20261115T051501_af533a.json`。
- 验证命令与实际结果：
  - `python -m cocoon.showcase`：`passed=true`，`contract=five_minute_showcase_v2`，主屏汉字计数 [28, 25, 32, 35]。
  - 四个关联套件（showcase/dashboard/closed_world_pilot/live_cross_topic_delivery）：**123 项 OK**。
  - `python -m cocoon validate`：**1050 项、0 failures / 0 errors / 0 skipped、success=true**（`experiment/review/validation_20261115T051501_af533a.json`；较步骤42 的 1031 项新增 19 项，全部来自 `test_showcase`）。
  - 回归后复跑 `tests.test_showcase`：19 项 OK；重新生成的页面字节不变。
  - 受保护原件 `dashboard.html`/`dashboard_data.json`/`verification.json` 前缀仍为 `46c6a0dc`/`6437e3a5`/`5397d08e`，账本 772 行（`e9ed802e…a322`），方案、`core.json`、`dashboard.py`、`closed_world_pilot.py`、封闭情境清单、旧讲稿哈希均未变。
  - Edge 无头离线巡检：视口约 1418×898 时舞台覆盖 0.817/0.817/0.791/0.817，无页面滚动；交互探针页面错误 0。
- 真实调用、用量与费用：无；**¥0.00**。
- 失败/偏差/尚未解决项：
  - 任务书写的“差值 ≤2.4%”与实测最大 2.60%（S02 R1）不符，页面按实测。
  - 任务书举例的“准点率98%”等短词不是原话子串，页面改用逐字子串。
  - 本机沙箱下 Python 不能覆盖已有文件：源码改动通过编辑器完成，生产 HTML 先删除再新建。
  - 无头模式虚拟时间不推进 CSS 动画和 SMIL，另用禁用动画的副本确认终态。
  - 结案 ZIP 不在本步范围内，未重建。
  - 真人审核仍为 0；账本 2 条持有预留待 `settle`；对话中出现过的密钥应作废。
- 下一步：由用户转达下一轮指令。演示页入口为 `python -m cocoon.showcase`（生成并核验），改样式后必须重跑并通过 `_ui_sandbox_audit`。汇报：[REPORT_step43_20261115.md](experiment/review/REPORT_step43_20261115.md)。

### 步骤44｜2026-11-15 14:40–15:45：5 分钟答辩演示页 v3（高定科学编辑部×精密光学沙盘重绘）正式入档
- 目的：针对用户反馈步骤43 `v2` 页面视觉“呆呆的、不高级”及本机 Playwright 截图复核发现的粗糙简笔造型与文字穿线碰撞缺陷，将演示页升级为高定科学编辑部×精密光学仪器级交互沙盘 `five_minute_showcase_v3`。**本步经用户明确指令（“这次你直接写代码，不用给 Codex”）并依 `AGENTS.md` 例外条款，由 Antigravity 直接执行。**
- 实际操作：重写 `cocoon/showcase.py` 视觉与 SVG 图元层，升级 `SHOWCASE_CONTRACT = "five_minute_showcase_v3"`，保持数据管线、只读来源与 `VALIDATION_PATH` 固定锚点不变。视觉重构：①暖象牙白宣纸底 `#F8F6F1`（暗场 `#0E1015`）、纯白圆角悬浮面板配 `<feDropShadow>` 柔和弥散投影、宋体衬线标题与等宽数字；②以双环认知核徽章 `_agent_node` 取代梯形路标火柴人，以双弧折射凸透镜 `_optical_lens` 取代死板等边三角形，废除 `3px 3px 0` 硬块阴影与外层黑框；③第 1 幕三列底边齐平、双圈反向公转培养皿与精密天平；④第 2 幕双弧认知镜经 5 条平滑水平三次贝塞尔光纤接入诊断条目卡，消除斜线穿字；⑤第 3 幕重构为四列横向圆角泳道，跨轨共享证据桥精确穿过泳道间隙（`y=360..394`），消除虚线劈穿字数；⑥第 4 幕采用 `±1.8px` 平行微偏移双轨 + 同心双色靶环 + 顶部独立回流区胶囊 + 胶囊哑铃图智能反向避让，消除混色与文字碰撞。门禁升级：`_ui_sandbox_audit` 新增 `ui_harsh_shadow_forbidden`、`ui_stick_figure_forbidden`、`ui_optical_defs_missing`。同步升级 `tests/test_showcase.py` 至 22 项，同步更新 `FIVE_MINUTE_SHOWCASE_SCRIPT_20261115.md`（保留 `…20261114.md` 与 `REPORT_step43_20261115.md` 不变）。
- 输入版本/文件：`dashboard_data.json`（`dataset_sha256=fc2ffd9b…9cd3`）、`closed_world_synth01_live_pilot.json`、`closed_world_pilot.build_closed_world_materials()`、固定归档报告 `validation_20261114T063037_ac1280.json`，均只读。
- 新增或修改文件：`cocoon/showcase.py`（137 413 字节，`c8b4b625…a67af`）；`tests/test_showcase.py`（22 项，18 398 字节，`86aceecb…3c120`）；`experiment/dashboard_20261110/showcase_5min.html`（352 858 字节，`461ad2a9…8c3d93`，`showcase_sha256=367b3685…8003f`）；`experiment/review/FIVE_MINUTE_SHOWCASE_SCRIPT_20261115.md`（`ae5d1ba1…92b98`）；`experiment/review/REPORT_step44_20261115.md`；`experiment/review/validation_20261115T074220_086089.json`（`9e1d8638…121e3`）。
- 验证命令（不含密钥）与实际结果：
  - `python -m cocoon.showcase`：`passed=true`，`contract=five_minute_showcase_v3`，主屏汉字计数 `[26, 25, 28, 30]`（上限 45），`rounds_checked=4`。
  - Playwright Chromium 离线无头十状态截图巡检（`1440×900`，`1.5x` DPR）：首轮发现第 4 幕右图 `Acc` 模式下回流区文字与 `100%` 打平标签重叠，回调至顶部网格线之上后重拍确认 10 张状态图全部零碰撞；`pageerror=[]`；四幕 `sh=900, sw=1440` 无滚动溢出。
  - 四个关联套件（showcase/dashboard/closed_world_pilot/live_cross_topic_delivery）：**126 项 OK**（548.299s）。
  - `python -m cocoon validate`：**1053 项、0 failures / 0 errors / 0 skipped、success=true**（`experiment/review/validation_20261115T074220_086089.json`；较步骤43 新增 3 项反简笔/光学门禁测试）。
  - 回归后复跑 `python -m unittest tests.test_showcase -v`：22 项 OK（3.302s），生产 HTML 字节与哈希 `461ad2a9…8c3d93` 不变。
  - 受保护原件 `dashboard.html`/`dashboard_data.json`/`verification.json` 前缀仍为 `46c6a0dc`/`6437e3a5`/`5397d08e`，账本 772 行（`e9ed802e…a322`），原方案、`core.json`、`dashboard.py`、`closed_world_pilot.py`、封闭清单、三议题矩阵、旧讲稿 `…20261114.md` 及 `REPORT_step43_20261115.md` 哈希均 100% 未变。
- 真实调用、用量与费用（如有）：无；**¥0.00**。
- 失败/偏差/尚未解决项：
  - 初次运行生成器时发现 `build_showcase_payload` 残留一行草稿推导式触发 `NameError`，立即删除修复；首轮截图发现第 4 幕 `Acc` 右图顶部两处文字同高重叠，立即分层修复并重拍确认。
  - 科研诚实边界与待复核项延续步骤42–43：受试为 `mimo-v2.6-flash`、每议题 `n=2`、真人受试与真人复核均为 `0`（`formal_eligible=False`）；主终点 `BS_T3` 打平（`0.0025`），盲区遗漏率 `O` 为 `I5` 33.3 优于 `I4` 58.3；S02 R1 `XL_E03`/`XL_E06` 错位待真人复核；账本 2 条持有预留合计 ¥2.103296 待 `settle`。
- 下一步：本步直接编码任务已完成，恢复 `AGENTS.md` 默认指挥官模式，等待用户下一轮指令。独立汇报：[REPORT_step44_20261115.md](experiment/review/REPORT_step44_20261115.md)。

## 4. 费用台账快照

以下为本机按公开价格和响应usage的保守记账，**不是平台最终账单**。缺少缓存明细时按未命中处理。

| 运行 | 实际HTTP次数 | 输入tokens | 输出tokens | 本机记账金额 |
|---|---:|---:|---:|---:|
| 连通性测试 | 1 | 45 | 6 | ¥0.000057 |
| 四阶段真实助手 | 4 | 15729 | 3387 | ¥0.022503 |
| 短投递v1失败尝试 | 1 | 2283 | 338 | ¥0.002959 |
| 短投递v2部分通过尝试 | 2 | 3679 | 355 | ¥0.004389 |
| 短投递v3部分通过尝试 | 2 | 4185 | 356 | ¥0.00439524 |
| 整句摘录式对照备选 | 0 | 0 | 0 | ¥0 |
| 步骤39连通性冒烟 | 1 | 45 | 6 | ¥0.00005700 |
| 步骤39真实组织侧（18次尝试：含5次本地校验拒绝、2轮重跑、1次中断） | 18 | 31991 | 3920 | ¥0.02151676 |
| 步骤40微型实证（4 次运行：3 次失败/中断 + 1 次完成） | 98 | 628128 | 62185 | ¥0.42873736 |
| 步骤40中断在途请求（用量未知，按最坏情况持有，未结算） | 1 | — | — | 持有 ¥1.050624 |
| 步骤41 TOPIC_02/03 真实实证（3 次运行：1 次失败 + 2 次完成） | 121 | 762039 | 76166 | ¥0.65358124 |
| 步骤42 §5.4 封闭情境实证（5 次运行：4 次失败/中断 + 1 次完成；136 次 HTTP，其中 1 次 HTTP 500 未结算） | 135 | 见账本 | 见账本 | ¥0.44355880 |
| 步骤42 HTTP 500 请求（用量未知，经用户授权按最坏情况持有，未结算） | 1 | — | — | 持有 ¥1.052672 |
| 累计（已结算） | **383** | 见账本 | 见账本 | **¥1.58175440** |

- 累计授权上限：¥5.00；剩余额度：**¥4.96569676**。
- 未决请求：0；未释放预留：¥0.00。
- 台账：`experiment/billing/mimo_initial_probe_v1.jsonl`。
- 不确定账单、预算不足或鉴权错误发生时停止；不得换新台账绕过。
- HTTP次数表示调用尝试；具体计费以可用usage和平台账单核对。上表十次均已有本机结算记录；v3普通侧512输入tokens命中缓存，按缓存单价记账，其他缺失缓存明细仍按未命中保守处理。

## 5. 测试与证据索引

### 全项目回归里程碑

| 报告 | 测试数 | 结果 | 范围说明 |
|---|---:|---|---|
| `experiment/review/validation_20261108T063747_f1e63a.json` | 406 | 通过 | MiMo集成阶段 |
| `experiment/review/validation_20261108T074703_9a2337.json` | 415 | 通过 | 候选证据制作阶段 |
| `experiment/review/validation_20261108T081818_08eeb0.json` | 478 | 通过 | 剂量设计稿阶段 |
| `experiment/review/validation_20261108T084744_2655bc.json` | 506 | 通过 | 真实输出审计阶段，早于短投递模块加入 |
| `tests/test_delivery.py`旧v1单独运行 | 30 | 历史开发测试通过 | 当时末次输入校验缺口尚未修复，现已由v2回归覆盖 |
| `experiment/review/validation_20261108T104347_89f97d.json` | 573 | 通过 | v2阶段全项目回归 |
| `experiment/review/validation_20261108T113453_b8882e.json` | 603 | 通过 | v3与摘录备选阶段的历史全项目回归 |
| `experiment/review/validation_20261108T123445_bbef07.json` | 644 | 通过，0失败/0错误/0跳过 | 步骤28历史全项目回归 |
| `experiment/review/validation_20261108T142436_14949a.json` | 683 | 0失败、4错误 | 步骤29首次回归；旧adapter事件文件追加时PermissionError，失败记录保留 |
| `experiment/review/validation_20261108T143449_f6add9.json` | 683 | 通过，0失败/0错误/0跳过 | 步骤29历史全项目回归 |
| `experiment/review/validation_20261108T150756_1871ae.json` | 723 | 通过，0失败/0错误/0跳过 | 步骤30历史全项目回归 |
| `experiment/review/validation_20261108T154323_08d340.json` | 749 | 通过，0失败/0错误/0跳过 | 步骤31首次全回归，后加强双分支闭环测试并再验 |
| `experiment/review/validation_20261108T155515_46ef93.json` | 749 | 通过，0失败/0错误/0跳过 | 步骤31历史全回归；66项测量测试（原40＋新26），含双分支完整链路 |
| `experiment/review/validation_20261109T025602_582dd0.json` | 771 | 通过，0失败/0错误/0跳过 | 步骤32历史全回归；22项网络级分析测试 |
| `experiment/review/validation_20261109T121218_e458e1.json` | 793 | 通过，0失败/0错误/0跳过 | 步骤33历史全回归；22项TOPIC_01三区材料包测试 |
| `experiment/review/validation_20261109T130342_7a6f52.json` | **808** | **通过，0失败/0错误/0跳过** | 最新全回归；37项三议题并行标准化材料包与模拟演练测试 |

各测试仅证明其检查范围；不能证明模型语义全正确、人工审核已完成、来源已获授权或实验有效。

### 便于继续工作的主要入口

| 用途 | 路径 |
|---|---|
| 本进度日志 | `PROGRESS.md` |
| 原方案 | `破茧助手全量实验方案_v1.md` |
| 主配置 | `configs/core.json` |
| 原助手冻结提示词 | `configs/assistant_prompts_v1.json` |
| 当前模型短投递提示词 | `configs/delivery_prompts_v3.json` |
| 摘录式对照策略 | `configs/extractive_control_v1.json` |
| 摘录式对照结果与审阅 | `experiment/review/delivery_v3_20261108/` |
| 六轮离线可行性（原件保留） | `experiment/review/cross_topic_20261108/feasibility.json` |
| 双人审核模板（原件保留） | `experiment/review/cross_topic_20261108/human_review_checklist.json` |
| 独立AI语境审阅（原件保留） | `experiment/review/cross_topic_20261108/independent_review.json` |
| 跨轮静态只读审阅页 | `experiment/review/cross_topic_20261108/review.html` |
| 本轮交付摘要与哈希 | `experiment/review/cross_topic_20261108/delivery.json` |
| 步骤28历史全项目报告 | `experiment/review/validation_20261108T123445_bbef07.json` |
| 步骤28历史离线交付包 | `experiment/exports/cross_topic_closeout_20261108.zip` |
| 步骤28原汇报（保留） | `experiment/review/cross_topic_20261108/REPORT_step28_20261108.md` |
| 双人审核工作流API | `cocoon/human_review.py` |
| 双人审核工作流专项测试 | `tests/test_human_review_workflow.py` |
| 步骤29历史全项目报告 | `experiment/review/validation_20261108T143449_f6add9.json` |
| 步骤29原汇报（保留） | `experiment/review/cross_topic_20261108/REPORT_step29_20261108.md` |
| 测量与盲评隔离API | `cocoon/measurement.py` |
| 测量专项测试 | `tests/test_measurement.py` |
| 步骤30历史全项目报告 | `experiment/review/validation_20261108T150756_1871ae.json` |
| 步骤30原汇报（保留） | `experiment/review/measurement_20261108/REPORT_step30_20261108.md` |
| 步骤31历史全项目报告 | `experiment/review/validation_20261108T155515_46ef93.json` |
| 步骤31原汇报（保留） | `experiment/review/measurement_20261108/REPORT_step31_20261108.md` |
| 网络级分析API | `cocoon/analysis.py` |
| 网络级分析专项测试 | `tests/test_analysis.py` |
| 步骤32历史全项目报告 | `experiment/review/validation_20261109T025602_582dd0.json` |
| 步骤32原汇报（保留） | `experiment/review/measurement_20261108/REPORT_step32_20261108.md` |
| TOPIC_01三区材料包API | `cocoon/pilot_materials.py` |
| 材料包与模拟演练专项测试 | `tests/test_pilot_materials.py` |
| 步骤33历史全项目报告 | `experiment/review/validation_20261109T121218_e458e1.json` |
| 步骤33原汇报（保留） | `experiment/review/pilot_materials_20261109/REPORT_step33_20261109.md` |
| 三议题全链路离线系统预演API | `cocoon/system_rehearsal.py` |
| 系统预演专项测试 | `tests/test_system_rehearsal.py` |
| 方案A双视角核验与放行API | `cocoon/ai_assisted_review.py` |
| 方案A专项测试 | `tests/test_ai_assisted_review.py` |
| 方案A已核验签发快照 | `experiment/review/ai_assisted_review_20261110/scheme_a_merged_verified.json` |
| 方案A快照导出脚本 | `scripts/export_scheme_a_snapshot.py` |
| 三议题可视化看板API | `cocoon/dashboard.py` |
| 看板专项测试 | `tests/test_dashboard.py` |
| 离线结案归档脚本 | `scripts/export_closeout_archive.py` |
| 看板单文件页面 | `experiment/dashboard_20261110/dashboard.html` |
| 看板派生数据包 | `experiment/dashboard_20261110/dashboard_data.json` |
| 看板§12.4验收报告 | `experiment/dashboard_20261110/verification.json` |
| 离线结案ZIP | `experiment/exports/cocoon_closeout_dashboard_20261110.zip` |
| 结案ZIP校验侧车 | `experiment/exports/cocoon_closeout_dashboard_20261110.zip.sha256` |
| 步骤36历史全项目报告 | `experiment/review/validation_20261111T061740_93ade4.json` |
| 六轮真实配对清单 | `experiment/review/live_cross_topic_20261111/six_round_live_extractive_pairs.json` |
| 真实组织侧运行目录 | `experiment/live_deliveries/`（含 `_aborted/` 中断运行） |
| 步骤40微型实证清单 | `experiment/review/live_micro_pilot_20261111/topic01_live_micro_pilot.json` |
| 步骤41 TOPIC_02/03 清单 | `experiment/review/live_micro_pilot_20261111/topic02_live_micro_pilot.json`、`topic03_live_micro_pilot.json` |
| 步骤41三议题矩阵 | `experiment/review/live_micro_pilot_20261111/three_topic_live_micro_pilot_matrix.json` |
| 步骤40真实运行目录 | `experiment/live_micro_pilot/`（4 个运行，3 个含 `aborted.json`） |
| 最新全项目验证报告 | `experiment/review/validation_20261115T074220_086089.json`（步骤44，1053 项通过） |
| 步骤43历史全项目报告 | `experiment/review/validation_20261115T051501_af533a.json`（步骤43，1050 项通过） |
| 步骤42历史全项目报告 | `experiment/review/validation_20261114T063037_ac1280.json`（1031 项；演示页固定引用此归档） |
| 步骤41历史全项目报告 | `experiment/review/validation_20261113T170455_6c3e4d.json` |
| 5 分钟演示沙盘（步骤44） | `experiment/dashboard_20261110/showcase_5min.html`（契约 v3，`cocoon/showcase.py` 生成与核验） |
| 5 分钟演示讲稿 | `experiment/review/FIVE_MINUTE_SHOWCASE_SCRIPT_20261115.md`（旧稿 `…20261114.md` 对应未入档 v1，保留） |
| 步骤40历史全项目报告 | `experiment/review/validation_20261113T090943_aee325.json` |
| 步骤39历史全项目报告 | `experiment/review/validation_20261111T132036_0447bf.json` |
| 步骤38历史全项目报告 | `experiment/review/validation_20261111T092930_d6cef2.json` |
| 步骤37历史全项目报告 | `experiment/review/validation_20261111T084340_5e169a.json` |
| 步骤38原汇报（保留） | `experiment/dashboard_20261110/REPORT_step38_20261110.md` |
| 步骤37原汇报（保留） | `experiment/dashboard_20261110/REPORT_step37_20261110.md` |
| 步骤36原汇报（保留） | `experiment/review/ai_assisted_review_20261110/REPORT_step36_20261110.md` |
| 步骤43原汇报（保留） | `experiment/review/REPORT_step43_20261115.md` |
| 本轮最新汇报（步骤44） | `experiment/review/REPORT_step44_20261115.md`（本步由 Antigravity 直接执行） |
| v2提示词（保留） | `configs/delivery_prompts_v2.json` |
| 短投递v1提示词（保留） | `configs/delivery_prompts_v1.json` |
| 候选证据包与审阅页 | `experiment/evidence_candidates/v1_20261108/build_20261108T074108_f38ec5/` |
| 原始来源底稿 | `experiment/evidence_candidates/v1_20261108/intake/` |
| 剂量编辑稿与审阅页 | `experiment/dose_candidates/dose_20261108T081317_cf1bb3/` |
| 真实四阶段运行 | `experiment/mimo_probes/assistant_probe_20261108T082120_9ad78cf8/` |
| 真实四阶段审阅 | `experiment/review/assistant_live_20261108/` |
| 最新模型短投递v3失败 | `experiment/delivery_probes/delivery_20261108T105552Z_7fe7dae9d342459885c811b169a74ff1/` |
| 短投递v2失败（保留） | `experiment/delivery_probes/delivery_20261108T101439Z_99cfd0db64294c3a8c51b1248b03eb98/` |
| 短投递v1失败（保留） | `experiment/delivery_probes/delivery_20261108T090523Z_fb38842073a64ca4ae95b42c082d6f7e/` |
| v3逐句AI审阅 | `experiment/review/delivery_v3_semantic.json` |
| v2逐句AI审阅（保留） | `experiment/review/delivery_v2_semantic.json` |
| 累计预算 | `experiment/billing/mimo_initial_probe_v1.jsonl` |
| 已交付压缩包 | `experiment/exports/` |

所有路径相对本项目根目录。上述旧产物保留其当时版本，不等于当前已全部满足正式实验条件。

## 6. 下一步与阻塞

### 下一次开发按此顺序接续

1. **先读本日志步骤44与 `experiment/review/REPORT_step44_20261115.md`**，默认恢复指挥官模式由用户转达下一轮指令。5 分钟演示页入口为 `python -m cocoon.showcase`（契约 `five_minute_showcase_v3`，生成并核验 `showcase_5min.html`）；改动样式或文案后必须重跑，并通过 `_ui_sandbox_audit`（零 Emoji、零渐变字、禁 `3px 3px 0` 硬块阴影、禁旧版梯形火柴人路径、光学渐变定义齐备、提词器与抽屉默认关闭、四幕沙盘、主屏汉字 ≤45）和 `_payload_truth_audit`。数据包固定引用 `validation_20261114T063037_ac1280.json`，不要改成扫描最新报告。以下为步骤43 时的接续说明：先读步骤43与 `experiment/review/REPORT_step43_20261115.md`。以下为步骤42 时的接续说明：**先读本日志步骤42与当轮 `REPORT_step42_20261114.md`、`FINAL_PROJECT_REPORT_20261114.md`**；封闭情境入口为 `closed_world_pilot.run_closed_world_live_pilot(execute=True)`（约 14 分钟，须后台运行）与 `verify_closed_world_live_pilot`；账本中 2 条持有预留（步骤40 中断、步骤42 HTTP 500）需拿到控制台用量后 `settle`；封闭情境 v2 须先预登记规则再运行，不得事后调参。以下为步骤41 时的接续说明：不自动扩展任务或收费。真实组织侧入口统一用 `live_cross_topic_delivery.run_remaining_live_organized_deliveries`（须显式 `execute=True`）与 `build_six_round_live_extractive_manifest` / `verify_six_round_live_extractive_manifest`；`MIMO_API_KEY` 只经环境变量传入，任何尝试都要留痕。真实微型实证入口用 `live_micro_pilot.run_topic_live_micro_pilot(topic_id, execute=True)`（每议题约 15–17 分钟，须单议题单命令后台运行）与 `verify_topic_live_micro_pilot`，三议题汇总用 `build/verify_three_topic_live_micro_pilot_matrix`；账本提额只能经 `BudgetLedger.raise_limit()` 追加事件；账本中 1 条中断持有预留需拿到控制台用量后 `settle`。看板入口统一用 `dashboard.build_dashboard_dataset` / `render_experiment_dashboard` / `verify_dashboard_bundle`，改样式后必须重跑 `render_experiment_dashboard` 与 `verify_dashboard_bundle` 并重建结案ZIP；`_ui_layout_audit` 会拦截胶囊撕裂、缺 `.chips` 容器、宽表无滚动保护、多 sticky 顶栏等回归。其展示数据是离线预演与方案A代理签发，不得当作真实实验结果或正式资格。
2. 六轮离线长度枚举、未填写人审模板和独立AI语境意见均已保存，不重复获取证据或重新生成这三份JSON。使用 `cross_topic_20261108/review.html` 阅读并按6项人审优先关注分配审核。
3. 两名不同真人独立填写各自副本，原模板保持不变；使用步骤29两个API核验与合并，分歧由独立第三人处理。尚需真实副本与实际身份核验；API不认证真人身份，当前55项110审核位全部未完成，AI意见不代替签字。
4. 若正式采用摘录式对照，须明确登记实现变更。六轮均有条件长度解，不代表五个缺实际组织输出的案例已成功，也不表示原v3已修复；不凭长度覆盖推断模型成功率。
5. 根据人工裁决处理11项原长报告AI问题与来源权利等待办，任何改动另存新版本、不覆盖原始模型结果。
6. 常规发言通道、匿名ID私有映射/回填、网络级统计与TOPIC_01三区材料包均已实现，仍须接实际可信事件/状态存储、评估器发送和真实面板。仅将public_blind_packets送盲评，私有registry摘要另存；旧测量自报桥接不能冒充常规发言。网络级p值只在有经scheduling.allocate重建的实际槽位分配时计算，且不得在无真实观测时解释为实验效应。步骤33的模拟审核不得直接落成人审通过，须由两名真人在各自另存副本上填写再走步骤29核验API；空白模板不得覆盖。真实T1、完整镜像、受试及评估模型、OASIS、其他干预臂和预实验范围/预算仍另行确认，正式实验关闭。
7. 每轮独立Markdown汇报与本进度日志同步更新，保留旧报告、失败历史和原始费用台账。

### 不能由本轮工程自动消除的阻塞

- 两名人工独立核验、译文与语义支持复核及分歧裁决尚未完成。
- 真实来源的使用和再分发权利仍待逐项确认。
- 三个候选轴目前是可兼容的侧重点，未验证为合理对立的量表；不据此报告U或立场极化效果。
- 每议题108张曝光/保持卡是工程目标，未完成；历史错误卡、锚题、迁移题与独立金标准尚未完整建立。
- OASIS接入、受试模型、评估模型、操作系统权限隔离、预实验预算及正式版本冻结未完成。
- AVeriTeC索引0接入仍保留原阻塞，不擅自绕过历史访问限制。

### 当前任务对应

| 任务 | 状态 | 接续点 |
|---|---|---|
| 6、10、13 | 阻塞/等待 | AVeriTeC原版本获取及索引0核对 |
| 1–5、7–9、11–39 | 已完成各自限定范围 | 不表示整个正式实验完成 |
| 40 | 已完成限定工程范围 | 报告/投递已分离，末次输入校验已修复并全项目回归通过 |
| 41 | 进行中 | v3已解决字段类型，但双模型长度仍失败；独立摘录备选不重标原模型运行成功 |
| 42 | 已交付本轮验收结果 | 提供v2原文、诊断、费用和阻塞；不是交付“整对已通过” |
| 43 | 已完成 | 已建立并核对本进度日志，后续持续追加 |
| 44 | 已完成限定范围 | v3类型提示已修、一次真实试跑已记录；普通侧长度仍失败，不算整体成功 |
| 45 | 进行中（历史交付收尾） | v3与摘录数据已留存；任务表尚未结案，本轮不代替其完整交付验收 |
| 49 | 进行中（历史任务） | 632/637摘录候选已构建，正式采用未确认，不标成完整实验通过 |
| 50 | 已完成限定范围 | 六轮离线可行性枚举，18项专项测试通过，不生成五轮缺失的真实组织侧 |
| 51 | 已完成模板整理 | 55项110人审位均pending，12项专项测试通过 |
| 52 | 已完成本轮限定交付 | 独立AI意见绑定、静态页面、644项回归与日志均已收尾，不等于人工批准 |
| 53、54 | 已完成限定代码范围 | 核对冻结输入并补充六轮离线函数及测试 |
| 55 | 已完成 | 双格式字节哈希严格兼容，真实独立审阅渲染在内的11项专项测试通过 |
| 56 | 已完成步骤28限定交付 | 644项历史全项目回归、配置登记、静态页、交付清单及独立Markdown汇报 |
| 57 | 已完成限定实现 | 两公共API及双人/第三人核验，不认证身份、不自动正式放行 |
| 58 | 已完成验证 | 39项新测试，最终683项全回归通过；首次4项旧写入错误记录保留 |
| 59 | 已完成步骤29汇报 | 步骤29独立MD与原件保留，真实人审0 |
| 60 | 已完成限定实现 | 测量、私有评分、盲评与T1自报桥接8接口，非真实观测 |
| 61 | 已完成验证 | 40项新测量测试，最新723项全项目通过 |
| 62 | 已完成步骤30汇报 | 步骤30独立MD保留，原件账本保持、新增费用0 |
| 63 | 已完成限定实现 | 常规发言桥接、私有registry与面板回填3API，旧8API保留 |
| 64 | 已完成验证 | 测量66项、最终全项目749项通过，合成双分支闭环，无真实效果观测 |
| 65 | 已完成本轮汇报 | 步骤31独立MD、core和本日志同步，原件保全、0调用0费用 |
| 66 | 已完成限定实现 | 新建analysis.py：网络聚合、2×2曝光、配对干预与实际槽位随机化检验 |
| 67 | 已完成验证 | 22项专项通过，最终全项目771项通过；reconcile→聚合→2×2闭环仅合成夹具 |
| 68 | 已完成本轮汇报 | REPORT_step32、core与PROGRESS步骤32同步，原件账本保全、0调用0费用 |
| 69 | 已完成契约核对 | 核实§5.1配额、96次排程可解与R2摘录区间差异 |
| 70 | 已完成限定实现 | pilot_materials.py三区材料包与§5.2八步模拟演练，人审0 |
| 71 | 已完成验证 | 22项专项通过，全项目 793 项通过，原件与人审模板空白状态保全 |
| 72 | 已完成本轮汇报 | REPORT_step33、core与PROGRESS步骤33同步，0调用0费用 |
| 73 | 已完成契约核对 | 三议题intake哈希与manifest一致、六轮剂量与摘录组合池可行 |
| 74 | 已完成限定实现 | 参数化三议题spec、4个新公共API、统一pilot_manifest与四道门限 |
| 75 | 已完成验证 | 37项专项通过，全项目 808 项通过，步骤28-33原件与空白模板保全 |
| 76 | 已完成本轮汇报 | REPORT_step34、core议题库规模与PROGRESS步骤34同步，0调用0费用 |
| 77 | 已完成契约核对 | 核对§6–11/13.4/15.1、四环境配额、六臂剂量、父子快照与网络级统计前置条件 |
| 78 | 已完成限定实现 | 新建 `cocoon/system_rehearsal.py`：四阶段合龙、六臂全量投递、双盲回填、2×2与T2/T3随机化Holm |
| 79 | 已完成验证 | 36项专项通过、全项目 844 项通过；第二次完整运行数值逐位一致 |
| 80 | 已完成本轮汇报 | REPORT_step35、core `system_rehearsal` 段与PROGRESS步骤35同步，0调用0费用、人审仍0 |
| 81 | 已完成契约核对 | 核对§5.2/§14.2/§15.1、55项分组、单列占用、角色互斥与合并件可写字段 |
| 82 | 已完成限定实现 | 新建 `cocoon/ai_assisted_review.py`：双视角副本、第三人裁决、权威合并、受控放行门禁 |
| 83 | 已完成验证 | 30项专项通过；110槽/55项/0未决/2角色列/内容与7门禁全通过；默认锁定vs授权解锁 |
| 84 | 已完成本轮汇报 | REPORT_step36、core `ai_assisted_review` 段与PROGRESS步骤36同步，0调用0费用、真人审核仍0 |
| 85 | 已完成契约核对 | 核对§12.1–12.4/§16、11视图数据需求、全链追溯键与无外链约束 |
| 86 | 已完成限定实现 | 新建 `cocoon/dashboard.py`：1248样本重建对账、11视图自包含HTML、§12.4验收 |
| 87 | 已完成验证 | 28项专项通过；25路径/130节点重放、网络与2×2/Holm重算、方案A重跑一致 |
| 88 | 已完成本轮汇报 | REPORT_step37、core `dashboard` 段、结案ZIP与PROGRESS步骤37同步，0调用0费用 |
| 89 | 已完成缺陷定位 | 复现胶囊半圆断裂与竖排：`.chip` 默认 inline 内含 block `small` 触发行内盒拆裂；`renderTimeline` 未用 `.chips` |
| 90 | 已完成修复 | `.chip` 改 `inline-flex` 列向；静态/动态时间轴统一 `.timeline-row`+`.chips`；9项 `ui_*` 审计入验收 |
| 91 | 已完成全视图升级 | 宽表 `.table-wrap`、`.net-grid` 3×2、单一 sticky `.topbar`、去重复 SVG、三断点实测0越界 |
| 92 | 已完成本轮汇报 | REPORT_step38、core `dashboard.ui_layout` 段、看板三件与结案ZIP重建，0调用0费用 |
| 93 | 已完成真实生成 | 5 轮 `mimo-v2.6-flash` 组织侧（11 次新调用）全部通过四句契约，落在可行区间 |
| 94 | 已完成配对合龙 | 6/6 清单、七项检查全通过；R1 复用；`prompt_variant` 与 3 处臂文本重合如实登记 |
| 95 | 已完成记账核对 | 账本 23→59 行，本步 ¥0.02157376，累计 ¥0.05587700，`reconciled=true` |
| 96 | 已完成接入与汇报 | pilot_materials/看板接入、27 项专项测试、REPORT_step39、core 与 PROGRESS 同步 |
| 97 | 已完成真实运行 | 4 次运行（3 失败/中断全部留痕），最终 52 次调用 0 被拒，16 测量 + 16 盲评回填 |
| 98 | 已完成账本处置 | 在途请求登记 interrupted 持有 ¥1.050624；单 ID 白名单门禁变更经用户授权并加测试 |
| 99 | 已完成清单与看板 | 清单离线重放通过；view-01/05/07/10 真实实证专区与 9b 重验；结案 ZIP 重建 |
| 100 | 已完成汇报 | REPORT_step40（天花板效应结论与 7 条诚实边界）、core 与 PROGRESS 同步 |
| 101 | 已完成提额 | `raise_limit` 事件与 5 项测试；共享账本 ¥5.00→¥50.00，原行字节保留 |
| 102 | 已完成真实运行 | TOPIC_02（1 次失败留痕 + 重跑完成）、TOPIC_03 完成；两条独立后台命令 |
| 103 | 已完成矩阵与看板 | 三议题矩阵离线核验通过；view-01/05/07/10 矩阵专区与 SVG 轨迹、9c 核验；结案 ZIP 重建 |
| 104 | 已完成汇报 | REPORT_step41、core 与 PROGRESS 同步 |

## 7. 后续更新约定

- 开始继续前先读第1节、第6节以及对应最新summary；新会话不只依赖聊天记忆。
- 2026-11-08起，用户安排由Gemini指挥后续工作：以用户转达的本轮指令为执行依据，不自行扩展实验或触发收费；每轮新增一份独立Markdown汇报，说明需求、改动、验证命令与报告路径、结果、保留文件哈希、费用及剩余阻塞。汇报保存在当轮输出目录，使用唯一文件名，不覆盖旧汇报；同时更新本日志。
- 每完成一个可独立验证的步骤，追加记录：**时间 → 目的 → 做了什么 → 文件/版本 → 实际检查结果 → 费用 → 阻塞/下一步**。
- 有新真实请求时立即记调用次数、usage、费用、失败阶段和原始记录路径；未知费用写“未知”，不能写0。
- 顶部状态与费用表可更新，历史失败记录不删。修复后另记“已修复”和新测试依据。
- 只有全项目测试实际跑完，才更新“最近全项目测试”；局部测试单独标注。
- 保留内部长报告、候选证据、编辑稿、真实输出、AI审阅、人审批准之间的身份区别。
- 不在此处写密钥、认证头、含密钥的完整命令或无关个人信息。
- 原始HTTP与详细事件继续留在JSON/JSONL中，本文件只做可读索引和事实摘要，不复制全部网页和模型原文。
- 未确认、不确定或尚未执行的操作明确标注；计划不是完成，结构通过不是语义通过，候选通过不是正式批准。

### 后续追加模板

```text
### 步骤NN｜YYYY-MM-DD HH:MM：步骤名称
- 目的：
- 实际操作：
- 输入版本/文件：
- 新增或修改文件：
- 验证命令（不含密钥）与实际结果：
- 真实调用、用量与费用（如有）：
- 失败/偏差/尚未解决项：
- 下一步：
```
