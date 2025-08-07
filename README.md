
## 🧩 插件简介

这是一个用于 Blender 的 SVG 导入插件，支持从剪贴板粘贴 SVG 文件，并自动添加立体效果。适用于快速将矢量图形转化为三维模型，提升建模效率。

![插件效果图](https://github.com/user-attachments/assets/086851aa-b8c2-48de-847f-74dae1f9814b)

---

## 🚀 功能亮点

- 直接从剪贴板粘贴 SVG 文件
- 一键导入并自动生成立体效果
- 无需手动转换或复杂操作
- 兼容 Blender 常规插件安装方式

---

## 🛠 安装方法

1. 打开 Blender，进入 `Edit > Preferences > Add-ons`
2. 点击右上角的 “Install” 按钮
3. 选择下载的插件 `.zip` 文件并安装
4. 勾选插件启用选项
5. 在工具栏中找到 “Paste SVG” 按钮，即可使用

---

## 📋 使用方法

1. 在任意矢量图软件中复制 SVG 图形（如 Adobe Illustrator、Inkscape）
2. 回到 Blender，点击插件中的 “Paste SVG” 按钮
3. 插件将自动解析 SVG 并生成立体模型
4. 可进一步编辑材质、厚度、位置等参数

---

## 📦 文件结构（可选）

如果你的插件包含多个文件，可以添加如下结构说明：

```
addons/
└── paste_svg_ma/
    ├── __init__.py
    ├── operator.py
    ├── panel.py
    ├── preferences.py
    └── utils.py
```

---

## 💡 示例项目（可选）


<img width="1445" height="1222" alt="image" src="https://github.com/user-attachments/assets/334ebf9f-e5e6-4a7a-8a7a-2b2c8f74f2c4" />

我们可以从svg图标库，支持复制为svg格式的矢量编辑软件直接复制，然后粘贴到blender里面





---

## 🧑‍💻 作者 & 贡献

由 [malongan](https://github.com/malongan) 开发。欢迎提交 Issue 或 Pull Request 改进插件功能。

---

