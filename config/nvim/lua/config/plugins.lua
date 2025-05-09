return {
  {
    "neovim/nvim-lspconfig", -- LSP конфигурация для Neovim
    config = function()
      -- Настроим LSP для Go
      require'lspconfig'.gopls.setup{
        settings = {
          gopls = {
            analyses = {
              unusedparams = true,
            },
            staticcheck = true,
          },
        },
      }
    end
  },
  {
    "hrsh7th/nvim-cmp", -- Автодополнение
    config = function()
      local cmp = require'cmp'
      cmp.setup({
        snippet = {
          expand = function(args)
            require('luasnip').lsp_expand(args.body)
          end,
        },
        mapping = cmp.mapping.preset.insert({
          ['<C-b>'] = cmp.mapping.scroll_docs(-4),
          ['<C-f>'] = cmp.mapping.scroll_docs(4),
          ['<C-Space>'] = cmp.mapping.complete(),
          ['<C-e>'] = cmp.mapping.close(),
          ['<CR>'] = cmp.mapping.confirm({ select = true }),
        }),
        sources = {
          { name = 'nvim_lsp' },
          { name = 'luasnip' },
        },
      })
    end
  },
  {
    "L3MON4D3/LuaSnip", -- Сниппеты
  },
  {
    "saadparwaiz1/cmp_luasnip", -- Интеграция LuaSnip с nvim-cmp
  },
}

