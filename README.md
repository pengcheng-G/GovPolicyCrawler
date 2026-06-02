# PolicyHarvester · 政策数据爬取工具

> 从政府网站批量抓取政策标题、发布时间、正文内容，用于经济政策分析与研究

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📌 项目背景

经济政策研究需要大量政府公开数据。手动复制粘贴效率低、易出错。本工具实现自动化批量抓取，帮助研究者快速构建政策数据库。

## 🎯 主要功能

- ✅ 读取 CSV 文件中的 URL 列表
- ✅ 自动提取网页标题 (`<title>`)
- ✅ 识别发布时间 (支持 `publishtime` 等常见标签)
- ✅ 抓取正文段落 (`<p>` 标签)
- ✅ 异常处理（网络错误、解析失败不影响整体）
- ✅ 输出结构化 CSV，便于后续分析

## 📁 输入格式

创建一个 `web.csv` 文件，至少包含两列（列名可自定义）：

| id | url |
|----|-----|
| 1  | https://www.gov.cn/zhengce/2023-01/01/content_12345.htm |
| 2  | https://www.ndrc.gov.cn/xxgk/zcfb/ghxwj/202301/t20230101_12345.html |

## 📤 输出格式

新增 `title`、`published_date`、`content` 三列：

| id | url | title | published_date | content |
|----|-----|-------|----------------|---------|
| 1  | ... | 关于...的通知 | 2023-01-01 | 正文内容... |

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/你的用户名/PolicyHarvester.git
cd PolicyHarvester
