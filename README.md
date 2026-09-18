<div align="center">

<img src="selected/x7rg_logo.png" alt="Logo oficial x7rG Enterprise" width="160" />

# Site do Adriano — Alicatado y Reforma en General

Landing page para o negócio de reformas do Adriano, em Vigo (Espanha).

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-online-15d5ae?style=for-the-badge&logo=github)](https://xx7rg.github.io/adriano-reformas-vigo/)

**[Ver site publicado](https://xx7rg.github.io/adriano-reformas-vigo/)**

</div>

---

## Estrutura

- `template.html` — o código-fonte editável: HTML + CSS + JavaScript puros
  (sem build step, sem dependências de npm/node). Este é o arquivo que você
  edita no VSCode. Já inclui `<!DOCTYPE html>`, `<html lang="es">` e
  `<meta charset>` completos.
- `build.py` — lê `template.html`, troca os placeholders `{{IMG_XX}}`,
  `{{LOGO_MARK}}`, `{{LOGO_WORD}}`, `{{X7RG_LOGO}}` e `{{HERO}}` pelas fotos
  correspondentes (convertidas para base64) e gera um único arquivo HTML
  autocontido em `dist/adriano-vigo-reformas.html` — pronto para hospedar em
  qualquer lugar sem precisar enviar mais nada junto.
- `build_web.py` — mesma ideia, mas gera `index.html` referenciando as fotos
  como arquivos separados em `selected/` (com `loading="lazy"`), em vez de
  embutir tudo em base64. É a versão usada no deploy do GitHub Pages — mais
  leve para carregar no celular.
- `selected/` — todas as fotos e logos usados pelo site.
- `aviso-legal.html` / `politica-privacidad.html` — páginas legais (LSSI-CE
  / RGPD), linkadas no rodapé do site.

## Como editar

1. Abra a pasta no VSCode.
2. Edite `template.html` normalmente (é HTML puro — recomendo a extensão
   "Live Server" do VSCode para pré-visualizar, mas repare que as tags
   `{{IMG_XX}}` só viram imagens de verdade depois de rodar um dos builds).
3. Depois de qualquer alteração, gere os arquivos finais rodando:

   ```bash
   python3 build.py       # gera dist/adriano-vigo-reformas.html (autocontido)
   python3 build_web.py   # gera index.html (usado no deploy do GitHub Pages)
   ```

4. Para publicar uma atualização no site já no ar, dê commit e push em
   `main` — o GitHub Pages faz o rebuild automaticamente.

## Requisitos

Só Python 3 (nenhuma biblioteca externa — `base64`, `os` e `mimetypes` já
vêm no Python padrão). Não precisa de Node, npm nem nenhum framework.

## Coisas importantes no código

- Paleta de marca em CSS custom properties no topo do `<style>`
  (`--navy`, `--orange`, `--cream`, etc.) — mude ali para afetar o site
  inteiro de uma vez.
- Cada seção do site é um `<section>` comentado (`HERO`, `SERVICIOS`,
  `COMO FUNCIONA`, `QUOTE BAND`, `COMPROMISO`, `GALERÍA`, `NOSOTROS`,
  `FOOTER`, etc.) — procure pelo comentário para achar a seção rápido.
- O JavaScript fica todo dentro de uma única tag `<script>` no final do
  arquivo, organizado em funções IIFE nomeadas (`initRadialButtons`,
  `initScrollReveal`, etc.) — cada uma cuida de uma interação específica.
- As fotos em `selected/img_XX.jpg` são referenciadas pelo número dentro da
  lista `items` — presente tanto em `build.py` quanto em `build_web.py` —
  para trocar ou adicionar uma foto na galeria, edite essa lista **nos dois
  arquivos**.
- O NIF do Adriano ainda está como `[pendiente de completar]` em
  `aviso-legal.html` e `politica-privacidad.html` — preencher assim que
  disponível.

---

<div align="center">

Desenvolvido por **x7rG Enterprise**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rgds/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_7ragnar/)

© 2026 x7rG ENTERPRISE™ — Todos os direitos reservados.

</div>
