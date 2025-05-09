function SetColor()
  -- Option 1
  -- vim.o.background = "dark"
  -- vim.cmd([[colorscheme gruvbox]])  

  -- Option 2
    vim.cmd.colorscheme "catppuccin"

    vim.api.nvim_set_hl(0, "Normal", { bg = "NONE" })
    vim.api.nvim_set_hl(0, "NormalNC", { bg = "NONE" })
    vim.api.nvim_set_hl(0, "SignColumn", { bg = "NONE" })
    vim.api.nvim_set_hl(0, "VertSplit", { bg = "NONE" })
    vim.api.nvim_set_hl(0, "EndOfBuffer", { bg = "NONE" })
end

SetColor()

