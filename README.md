# 🌵Cactus: A macOS App to Extract Texts from Links

![m1Xnm10](https://i.imgur.com/m1Xnm10.png)

Cactus is a macOS app to extract texts from links.

Cactus 是一个 macOS 上的小软件，用来获取链接中的文字。

## 解决问题

复制链接里面的文字实在是太麻烦了，很多方法已经失效：
1. 使用一些浏览器扩展，但是有些都失效了，少数几个还能用……更别提许多浏览器扩展只对应特定框架的浏览器；
2. 按住 Alt 键，或者 Option 键（mac 上），虽然能选择，但选完了还是会打开链接、弹出新页面，而且 Safari 不支持此操作。
所以我想，既然超链接的文本都有右键全选的功能，那么可不可以做一款跨越浏览器的、简单轻量的文本选取器？于是 Cactus 就诞生了。

## 功能亮点

### 选取链接中的部分文本：

Cactus 当然可以复制一个链接中的全部文本，但更关键的是，它可以获取这个链接中间的某些文字。当我们看到一个超链接文本的中部有我们需要的文字，但苦于无法获取它的时候——例如在搜索引擎的结果界面上——Cactus 就能快速地满足需求：用户可用光标在弹出的文本框内选中一部分文字，然后点击“Copy selected”按钮即可。

### 对部分文本进行实时修改：

既然 Cactus 能够复制全部文本，那么在文本框中对这部分文字加以修改如何呢？Cactus 也能胜任。有些时候，我们对我们刚刚获取到的文字需要进行快速简单的加工，例如增添一些语气词，或者将其填补完整、成为一句完整的话，这时，Cactus 就相当于是一个实时的剪贴板编辑器，用户可以随心所欲地编辑出想要的文字，然后点击“Copy all”按钮，那么刚刚修改过的文本就全部复制到剪贴板了。

## 界面一览

<p align="center">
  <img src="https://i.imgur.com/sWrcqeu.png" width=400 />
</p>

## DEMO

https://github.com/Ryan-the-hito/Cactus/assets/95213517/a26ae65e-90ec-41d5-b352-e2bcf1d38156

## 环境要求

- MacOS 11 及以上（测试环境为 MacOS 12.6.5）
- M1、M2 芯片

## 下载安装

从 Release 里面下载压缩包，之后将解压好的 app 文件拖入程序文件夹中。

Cactus 将需要辅助权限以完整运行：

<p align="center">
  <img src="https://i.imgur.com/dXjKePY.png" width=400 />
</p>


在弹出上述权限需求后，用户可打开设置界面，在辅助权限一项中选择 Cactus。

<p align="center">
  <img src="https://i.imgur.com/rEvUmO3.png" width=400 />
</p>


上述设置之后，用户可以点击 Cactus 在任务栏中的图标，点击“Settings”，设置延迟时间。延迟时间表示的是从用户点击“🌵 Get text from links!”之后，直到将光标停留在待选链接上的时间。由于用户需要将光标从任务栏移动到浏览器内的指定位置，这还需要一段距离，因此设置了此延迟时间。该值默认为 0，单位为秒，可以根据需要设置，只可为整数。

## 使用说明

### 方法一：手动点击触发

用户先点击 Cactus 在任务栏中的图标，在下拉选单中点击“🌵 Get text from links!”，然后在延迟时间之内将光标移动到链接上，此时光标将从箭头形状变为手套形状，这表示已在链接可选区域之上。

在延迟时间达至之后，Cactus 将运行程序，弹出窗口，显示该链接内的文本，用户可以选择部分，或是修改后选择全部。

### 方法二：启动器快捷键触发

用户可以使用 Alfred 或者 BetterTouchTool 等脚本工具来使上述过程自动化。上述可被归纳为两个动作，一是触发命令，二是移动鼠标。触发命令可由脚本自动完成，用户只需将鼠标先移动到链接之上，然后再触发脚本，即可更快速地获取链接文本。Release 中自带“Cactus Keyword to Script.alfredworkflow”和“Show Cactus.applescript”两个文件，其中前者是 Alfred 的指令文件，若用户电脑已有 Alfred 软件，即可安装此指令使用（可在 Alfred 内设置全局快捷键）；后者是通用的 Applescript 脚本，用户需要在其习惯的启动器中设置此脚本的触发模式。

### 方法三：第三方 Touch Bar

在使用 MTMR、BetterTouchTool 等客制化 Touch Bar 软件时，用户可以自定义 Touch Bar 按键，以一键触发。以下是适用于 MTMR 的配置。

```JSON
{
    "type": "staticButton",
    "align": "right",
    "title": “Button",
    "bordered": true,
    "width": 44,
    "action": "appleScript",
    "actionAppleScript": {
      "filePath": “[YOUR PATH TO Show Cactus.applescript]",
    },
}
```

## 注意事项

1. Cactus 只能在多个浏览器和网页页面中使用，可能并不适用于其他软件，如聊天软件等；
2. 如果不是超链接形态的文字，那么使用 Cactus 并不会十分见效，比如一些限制复制的文本，使用 Cactus 也无法见效；
3. 最好配合 Alfred、BetterTouchTool 等启动器软件一并使用，通过快捷键或者 Applescript 脚本触发软件执行。除此之外，还可以使用 Touch Bar 来触发，可在 MTMR、BetterTouchTool 中设置。如果没有上述软件工具，可在设置的第一项中设置等待时间，以确定在触发后多久读取鼠标位置的文本信息。
4. 如果遇见右键菜单弹出速度慢，以至于无法快速获取剪贴板内容，请适当调整设置中的参数，以达至较好的效果；
5. 更新后需要重新在设置中为软件授予辅助权限。

## 证书信息

GPL-3.0 license

## 特别致谢

1. [Qt](https://github.com/qt)本软件遵守 Qt 的开源协议。

## 支持作者

<p align="center">
  <img src="https://i.imgur.com/OHHJD4y.png" width=240 />
  <img src="https://i.imgur.com/6XiKMAK.png" width=240 />
</p>
