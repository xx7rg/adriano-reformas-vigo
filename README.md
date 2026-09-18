# Site do Adriano — Alicatado y Reforma en General

Site de página única (landing page) para o negócio do Adriano em Vigo, Espanha.

## Estrutura

- `template.html` — o código-fonte editável: HTML + CSS + JavaScript (sem build step,
  sem dependências de npm/node). Este é o arquivo que você edita no VSCode.
- `build.py` — script Python que lê `template.html`, troca os placeholders
  `{{IMG_XX}}`, `{{LOGO_MARK}}`, `{{LOGO_WORD}}`, `{{X7RG_LOGO}}` e `{{HERO}}`
  pelas fotos correspondentes (convertidas para base64) e gera um único
  arquivo HTML autocontido, pronto para hospedar em qualquer lugar.
- `selected/` — todas as fotos e logos usados pelo site.

## Como editar

1. Abra a pasta no VSCode.
2. Edite `template.html` normalmente (é HTML puro — recomendo a extensão
   "Live Server" do VSCode para pré-visualizar, mas repare que as tags
   `{{IMG_XX}}` só viram imagens de verdade depois de rodar o `build.py`).
3. Depois de qualquer alteração, gere o arquivo final rodando:

   ```bash
   python3 build.py
   ```

   Isso cria `adriano-vigo-reformas.html` (o arquivo pronto para publicar)
   na pasta `dist/` (veja abaixo — ajustei o caminho de saída para ficar
   dentro do próprio projeto).

4. Esse arquivo `.html` final é 100% autocontido (todas as imagens embutidas
   em base64) — pode subir direto para qualquer hospedagem estática
   (Netlify, Vercel, GitHub Pages, cPanel, etc.) sem precisar enviar mais
   nada junto.

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
  lista `items` no topo do `build.py` — para trocar ou adicionar uma foto
  na galeria, edite essa lista.
