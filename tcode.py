__author__ = 'ping'
import re

ts = '''
			{% for row1 in tab1 %}
            this.label{{row1.col1}} = new System.Windows.Forms.Label();
			{%endfor%}
			{% for row1 in tab1 %}
            this.textBox{{row1.col1}} = new System.Windows.Forms.TextBox();
			{%endfor%}
            this.btnMoveNext = new System.Windows.Forms.Button();
            this.btnMovePrev = new System.Windows.Forms.Button();
            this.btnSave = new System.Windows.Forms.Button();
			{% for row1 in tab1 %}
			this.label{{row1.col1}}.AutoSize = true;
            this.label{{row1.col1}}.Location = new System.Drawing.Point(7, {{row1.col3}});
            this.label{{row1.col1}}.Name = "label{{row1.col1}}";
            this.label{{row1.col1}}.Size = new System.Drawing.Size(55, 15);
            this.label{{row1.col1}}.Text = "{{row1.col2}}";

			{%endfor%}

			{% for row1 in tab1 %}
	        this.textBox{{row1.col1}}.Font = new System.Drawing.Font("微软雅黑", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.textBox{{row1.col1}}.Location = new System.Drawing.Point(88, {{row1.col3}});
            this.textBox{{row1.col1}}.Name = "textBox{{row1.col1}}";
            this.textBox{{row1.col1}}.Size = new System.Drawing.Size(201, 29);
            this.textBox{{row1.col1}}.TabIndex = {{row1.col4}};
            this.textBox{{row1.col1}}.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;

			{%endfor%}
  //
            // btnMoveNext
            //
            this.btnMoveNext.Location = new System.Drawing.Point(305, 14);
            this.btnMoveNext.Name = "btnMoveNext";
            this.btnMoveNext.Size = new System.Drawing.Size(75, 23);
            this.btnMoveNext.TabIndex = 21;
            this.btnMoveNext.Text = "下一条";
            this.btnMoveNext.UseVisualStyleBackColor = true;
            this.btnMoveNext.Click += new System.EventHandler(this.btnMoveNext_Click);
            //
            // btnMovePrev
            //
            this.btnMovePrev.Location = new System.Drawing.Point(386, 14);
            this.btnMovePrev.Name = "btnMovePrev";
            this.btnMovePrev.Size = new System.Drawing.Size(75, 23);
            this.btnMovePrev.TabIndex = 22;
            this.btnMovePrev.Text = "上一条";
            this.btnMovePrev.UseVisualStyleBackColor = true;
            this.btnMovePrev.Click += new System.EventHandler(this.btnMovePrev_Click);
            //
            // btnSave
            //
            this.btnSave.Location = new System.Drawing.Point(468, 14);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(75, 23);
            this.btnSave.TabIndex = 23;
            this.btnSave.Text = "保存数据";
            this.btnSave.UseVisualStyleBackColor = true;
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);

			{% for row1 in tab1 %}
			this.Controls.Add(this.label{{row1.col1}});
			{%endfor%}
			{% for row1 in tab1 %}
            this.Controls.Add(this.textBox{{row1.col1}});
			{%endfor%}
            this.Controls.Add(this.btnSave);
            this.Controls.Add(this.btnMovePrev);
            this.Controls.Add(this.btnMoveNext);

		{% for row1 in tab1 %}
		private System.Windows.Forms.Label label{{row1.col1}};
		{%endfor%}
		{% for row1 in tab1 %}
        private System.Windows.Forms.TextBox textBox{{row1.col1}};
		{%endfor%}
        private System.Windows.Forms.Button btnMoveNext;
        private System.Windows.Forms.Button btnMovePrev;
        private System.Windows.Forms.Button btnSave;
'''
ts = ts.strip()
ts = ts.replace('%}\n', '%}')
ts = ts.replace('%}\r\n', '%}')

rs = """
<replace>
XXX = Account
title = Account管理
controller = Account
表名 = Account
名称空间 = HYKJ
模型 = TbAccount
</replace>
<tab1>
Id	Id	13	1
AcountDate	记账日期	43	2
DateText	DateText	73	3
AcountType	账目类型	103	4
IsIncome	IsIncome	133	5
AccountContent	账目名称	163	6
Amount	金额	193	7
</tab1>
"""
reg = re.compile(r'\b(.+?)\s+=\s+(.+?)\b')
g = reg.findall(rs)
reg1 = re.compile(r'<(tab.+?)>([\s\S]+?)</(tab.+?)>')
g1 = reg1.findall(rs)
tc = dict(g)
print(g1)
reg3 = re.compile(r'[\t\s,;]+')
for item in g1:
    tabName = item[0]
    tabRows = item[1].strip()
    rowList = tabRows.split('\n')
    objList = []
    for row in rowList:
        colNames = {}
        parts = reg3.split(row)
        for i, p in enumerate(parts):
            idx = 'col' + '{0}'.format(i + 1)
            colNames[idx] = p
        objList.append(colNames)
    tc[tabName] = objList
print(tc)