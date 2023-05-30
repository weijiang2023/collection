// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AI原优舍',
  tagline: "业界领先的人工智能时尚买手专门店",
  url: 'https://your-docusaurus-test-site.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'AI原优舍',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'news',
            position: 'left',
            label: '时尚快报',
          },
          {
            type: 'doc',
            docId: 'selection.ling',
            position: 'left',
            label: '玲选',
          },
          {
            type: 'doc',
            docId: 'selection.bing',
            position: 'left',
            label: '冰选',
          },
          {
            type: 'doc',
            docId: 'tgif',
            position: 'right',
            label: '现代汉服原创设计',
          },
          {
            type: 'doc',
            docId: 'polo',
            position: 'right',
            label: 'Polo',
          },
          {
            type: 'doc',
            docId: 'about',
            position: 'right',
            label: '关于我们',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: '潮流单品',
            items: [
              {
                label: '男装',
                to: '/docs/products/man',
              },
              {
                label: '女装',
                to: '/docs/products/lady',
              },
              {
                label: '童装',
                to: '/docs/products/child',
              },
              {
                label: '其他',
                to: '/docs/products/others',
              },
            ],
          },
          {
            title: '核心团队',
            items: [
              {
                label: '小玲买手',
                to: '/docs/buyers/ling',
              },
              {
                label: '小冰买手',
                to: '/docs/buyers/bing',
              },
              {
                label: '小江技术',
                to: '/docs/buyers/jiang',
              },
            ],
          },
          {
            title: '核心技术',
            items: [
              {
                label: 'mix & match',
                to: '/docs/tech/mm',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} AI原优舍. Built with 大爱 and powered by 算法妈妈`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
