Project tree: 
```        ├── .gitattributes
        ├── .gitignore
        ├── .prettierrc.json
        ├── README.md
        ├── README_fr.md
        ├── bloomscape.sqlite
        ├── bloomscape_roadmap.pdf
        ├── env.d.ts
        ├── index.html
        ├── public/
        │   ├── bloomscape_logo.png
        │   ├── bloomscape_market_presentation.wav
        │   ├── bloomscape_presentation.wav
        │   ├── bloomscape_text.png
        │   ├── favicon.ico
        │   ├── favicon.png
        │   └── textures/
        │       ├── land_bottom.png
        │       ├── land_grass_side.png
        │       ├── soil_center.png
        │       ├── soil_corner.png
        │       ├── soil_edge.png
        │       └── water/
        │           ├── 1side/
        │           │   ├── frame1.png
        │           │   ├── frame10.png
        │           │   ├── frame11.png
        │           │   ├── frame12.png
        │           │   ├── frame13.png
        │           │   ├── frame14.png
        │           │   ├── frame15.png
        │           │   ├── frame16.png
        │           │   ├── frame2.png
        │           │   ├── frame3.png
        │           │   ├── frame4.png
        │           │   ├── frame5.png
        │           │   ├── frame6.png
        │           │   ├── frame7.png
        │           │   ├── frame8.png
        │           │   └── frame9.png
        │           ├── 2sides/
        │           ├── 3sides/
        │           ├── 4sides/
        │           ├── open/
        │           │   ├── frame1.png
        │           │   ├── frame10.png
        │           │   ├── frame11.png
        │           │   ├── frame12.png
        │           │   ├── frame13.png
        │           │   ├── frame14.png
        │           │   ├── frame15.png
        │           │   ├── frame16.png
        │           │   ├── frame2.png
        │           │   ├── frame3.png
        │           │   ├── frame4.png
        │           │   ├── frame5.png
        │           │   ├── frame6.png
        │           │   ├── frame7.png
        │           │   ├── frame8.png
        │           │   └── frame9.png
        │           └── xcf_files/
        │               ├── frame1.xcf
        │               ├── frame10.xcf
        │               ├── frame11.xcf
        │               ├── frame12.xcf
        │               ├── frame13.xcf
        │               ├── frame14.xcf
        │               ├── frame15.xcf
        │               ├── frame16.xcf
        │               ├── frame2.xcf
        │               ├── frame3.xcf
        │               ├── frame4.xcf
        │               ├── frame5.xcf
        │               ├── frame6.xcf
        │               ├── frame7.xcf
        │               ├── frame8.xcf
        │               └── frame9.xcf
        ├── src/
        │   ├── App.vue
        │   ├── BaseApp.vue
        │   ├── assets/
        │   │   ├── globals.css
        │   │   └── main.css
        │   ├── components/
        │   │   ├── FlowerImage.vue
        │   │   ├── Footer.vue
        │   │   ├── Form.vue
        │   │   ├── GlobalModal.vue
        │   │   ├── Header.vue
        │   │   ├── HomeMarketTicker.vue
        │   │   ├── admin/
        │   │   │   ├── AdminSideBar.vue
        │   │   │   └── integrated_views/
        │   │   │       ├── AdminConfig.vue
        │   │   │       ├── AdminDatabase.vue
        │   │   │       ├── AdminLogs.vue
        │   │   │       ├── AdminModeration.vue
        │   │   │       ├── AdminOverview.vue
        │   │   │       ├── AdminReports.vue
        │   │   │       └── AdminUsers.vue
        │   │   ├── auth/
        │   │   │   ├── AuthModal.vue
        │   │   │   └── logic/
        │   │   │       └── useAuthModal.ts
        │   │   ├── buttons/
        │   │   │   ├── GoogleLoginBtn.vue
        │   │   │   └── ThemeSwitcher.vue
        │   │   ├── chat/
        │   │   │   └── GlobalChatDrawer.vue
        │   │   ├── game/
        │   │   │   ├── LandScene.vue
        │   │   │   ├── SideBar.vue
        │   │   │   ├── TopBar.vue
        │   │   │   ├── config/
        │   │   │   │   └── ItemRegistery.ts
        │   │   │   ├── logic/
        │   │   │   │   ├── AutoTilingUtils.ts
        │   │   │   │   ├── LandSceneManager.ts
        │   │   │   │   └── WorldElementsManager.ts
        │   │   │   └── modal_features/
        │   │   │       ├── InventoryInModal.vue
        │   │   │       └── MarketInModal.vue
        │   │   └── icons/
        │   │       ├── DiscordIcon.vue
        │   │       ├── InstagramIcon.vue
        │   │       └── navbar/
        │   │           ├── HomeIcon.vue
        │   │           ├── InventoryIcon.vue
        │   │           ├── MarketIcon.vue
        │   │           └── SettingsIcon.vue
        │   ├── main.ts
        │   ├── private/
        │   │   └── assets/
        │   │       ├── flowers/
        │   │       │   ├── golden_lotus/
        │   │       │   │   ├── icon/
        │   │       │   │   │   └── seed.png
        │   │       │   │   └── sprite/
        │   │       │   │       └── seed.png
        │   │       │   ├── heart_flower/
        │   │       │   │   └── icon/
        │   │       │   │       ├── growing1.png
        │   │       │   │       ├── growing2.png
        │   │       │   │       ├── mature.png
        │   │       │   │       ├── seed.png
        │   │       │   │       ├── sprout1.png
        │   │       │   │       ├── sprout2.png
        │   │       │   │       └── withered.png
        │   │       │   ├── night_shade/
        │   │       │   └── unknown.png
        │   │       └── items/
        │   ├── routes/
        │   │   ├── index.ts
        │   │   ├── routes_enum.ts
        │   │   └── scroll.ts
        │   ├── server/
        │   │   ├── _seedMarket.ts
        │   │   ├── api.ts
        │   │   ├── controllers/
        │   │   │   ├── AdminController.ts
        │   │   │   ├── AuthController.ts
        │   │   │   ├── ChatController.ts
        │   │   │   ├── GameController.ts
        │   │   │   ├── MarketController.ts
        │   │   │   ├── ReportController.ts
        │   │   │   └── UserController.ts
        │   │   ├── ext.ts
        │   │   └── index.ts
        │   ├── shared/
        │   │   ├── analytics/
        │   │   │   ├── FlowerDiscovery.ts
        │   │   │   ├── ModerationLog.ts
        │   │   │   └── UserReport.ts
        │   │   ├── chat/
        │   │   │   ├── Chat.ts
        │   │   │   ├── ChatMessage.ts
        │   │   │   └── ChatParticipant.ts
        │   │   ├── economy/
        │   │   │   ├── Item.ts
        │   │   │   ├── MarketHistory.ts
        │   │   │   ├── MarketListing.ts
        │   │   │   ├── MarketStat.ts
        │   │   │   └── SapPurchase.ts
        │   │   ├── flowers/
        │   │   │   ├── FlowerSpecies.ts
        │   │   │   └── UserFlower.ts
        │   │   ├── index.ts
        │   │   ├── map/
        │   │   │   ├── Island.ts
        │   │   │   └── Tile.ts
        │   │   ├── social/
        │   │   │   ├── ClaimLink.ts
        │   │   │   ├── Friendship.ts
        │   │   │   └── UserClaim.ts
        │   │   ├── types.ts
        │   │   └── user/
        │   │       ├── Achievement.ts
        │   │       ├── User.ts
        │   │       ├── UserAchievement.ts
        │   │       └── UserItem.ts
        │   ├── stores/
        │   │   ├── auth.ts
        │   │   ├── breakpoints.ts
        │   │   ├── chat.ts
        │   │   ├── game.ts
        │   │   ├── modal.ts
        │   │   ├── theme.ts
        │   │   └── ui.ts
        │   └── views/
        │       ├── AboutView.vue
        │       ├── ContactView.vue
        │       ├── HomeView.vue
        │       ├── WikiView.vue
        │       ├── admin/
        │       │   ├── DBManagerView.vue
        │       │   └── ManagerView.vue
        │       ├── errors/
        │       │   └── 404View.vue
        │       ├── game/
        │       │   ├── FloraDexView.vue
        │       │   ├── LandView.vue
        │       │   ├── LeaderboardView.vue
        │       │   ├── MarketView.vue
        │       │   └── UserProfileView.vue
        │       └── user/
        │           ├── LoginView.vue
        │           ├── SettingsView.vue
        │           ├── SignupView.vue
        │           └── SupportView.vue
        ├── tsconfig.app.json
        ├── tsconfig.json
        ├── tsconfig.node.json
        └── vite.config.ts
```
---
### File: .gitattributes
---

```text
* text=auto eol=lf

```

---
### File: .gitignore
---

```text
# VSCode 
.vscode/

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

**/.env

node_modules
.DS_Store
dist
dist-ssr
coverage
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

*.tsbuildinfo

.eslintcache

# Cypress
/cypress/videos/
/cypress/screenshots/

# Vitest
__screenshots__/

# Database & private
*.sqlite
src/private/**
```

---
### File: .prettierrc.json
---

```json
{
  "$schema": "https://json.schemastore.org/prettierrc",
  "semi": false,
  "singleQuote": true,
  "printWidth": 100
}

```

---
### File: README.md
---

```md
# 🌸 BloomScape

(first version of this README made with AI, errors may exist)

**BloomScape** is a relaxing and strategic online gardening simulation game. Manage your garden, cultivate rare species, and trade your harvests in a dynamic market within a closed economy.

## 🌟 Key Features

- 🌱 **Garden Management:** Plant, water, and grow your flowers in real-time. Careful, without care, they wither!
- 💎 **Rarity System:** Discover species of varying rarity, from common to legendary flowers.
- 💰 **Player-vs-Player Market:** Sell your finest harvests for **Sap** (virtual currency) or buy missing flowers for your collection: beware, species prices can fluctuate.
- 🏆 **Progression:** Level up to unlock new seeds and expand your land.
- 📖 **Floradex:** Complete your botanical collection album.

## ⚖️ License & Copyright

**© 2025 BloomScape. All rights reserved.**

This source code is made public **solely for educational, demonstration, and transparency purposes**.

- You are authorized to view the code to learn or audit its functionality.
- **You are NOT authorized** to copy, modify, distribute, sell, or use this code for a commercial or personal project (made public) without explicit written permission from the author.
- Some graphic assets are missing from the code, and are replaced by a placeholder.

---

_Made with ❤️ and fresh water by BloomScape._

```

---
### File: README_fr.md
---

```md
# 🌸 BloomScape

(première version de ce README faite avec IA, il peut y avoir des erreurs)

**BloomScape** est un jeu de simulation de jardinage en ligne relaxant et stratégique. Gérez votre jardin, cultivez des espèces rares et échangez vos récoltes sur un marché dynamique au sein d'une économie fermée.

## 🌟 Fonctionnalités Clés

- 🌱 **Gestion de Jardin :** Plantez, arrosez et faites grandir vos fleurs en temps réel. Attention, sans soin, elles fanent !
- 💎 **Système de Rareté :** Découvrez des espèces de différentes rareté, des plus communes aux fleurs légendaires.
- 💰 **Marché Joueur-contre-Joueur :** Vendez vos plus belles récoltes contre de la **Sève** (monnaie virtuelle) ou achetez les fleurs manquantes à votre collection : attention le prix d'une espèce peut évoluer.
- 🏆 **Progression :** Montez de niveau pour débloquer de nouvelles graines et agrandir votre terrain.
- 📖 **Floradéx :** Complétez votre album de collection botanique.

## ⚖️ License & Copyright

**© 2025 BloomScape. Tous droits réservés.**

Ce code source est rendu public **uniquement à des fins éducatives, de démonstration et de transparence**.

- Vous êtes autorisé à consulter le code pour apprendre ou auditer le fonctionnement.
- **Vous n'êtes PAS autorisé** à copier, modifier, distribuer, vendre ou utiliser ce code pour un projet commercial ou personnel (rendu publique) sans autorisation écrite explicite de l'auteur.
- Certains assets graphiques sont manquants dans le code, et sont remplacés par un placeholder.

---

_Fait avec ❤️ et de l'eau fraîche par BloomScape._

```

---
### File: env.d.ts
---

```ts
/// <reference types="vite/client" />

```

---
### File: index.html
---

```html
<!doctype html>
<html lang="en" data-theme="forest">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"
    />
    <title>BloomScape</title>

    <!-- GOOGLE-API INIT -->
    <script src="https://accounts.google.com/gsi/client" async defer></script>
  </head>

  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>

```

---
### File: src/App.vue
---

```vue
<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import Base from './BaseApp.vue'
import { onMounted } from 'vue'
import AuthModal from './components/auth/AuthModal.vue'
import { useAuthModal } from '@/components/auth/logic/useAuthModal'

import GlobalModal from './components/GlobalModal.vue'
import GlobalChatDrawer from './components/chat/GlobalChatDrawer.vue'

const auth = useAuthStore()

const { isOpen, mode, handleSuccess } = useAuthModal()

onMounted(async () => {
  await auth.fetchSessionUser()
})
</script>

<template>
  <AuthModal v-model:is-open="isOpen" :mode="mode" @success="handleSuccess" />
  <GlobalModal />
  <GlobalChatDrawer />

  <Base>
    <RouterView />
  </Base>
</template>

```

---
### File: src/BaseApp.vue
---

```vue
<script setup lang="ts">
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import { onMounted } from 'vue'
import { useThemeStore } from '@/stores/theme'
import { useRoute } from 'vue-router'

const themeStore = useThemeStore()

onMounted(() => {
    themeStore.applyTheme()
})

const route = useRoute()
</script>

<template>
    <Header v-if="!route.meta.hideLayout" />

    <main class="container mx-auto h-full flex flex-col gap-10 items-center justify-center">
        <slot />
    </main>

    <Footer v-if="!route.meta.hideLayout" />
</template>

```

---
### File: src/assets/globals.css
---

```css
@import 'tailwindcss';

@plugin "daisyui" {
  themes: forest --default --prefersdark;
}

@theme {
  --breakpoint-phone: 450px;
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;

  --color-bloom-primary: #34d399;
  --color-bloom-secondary: #10b981;
  --color-bloom-dark: #022c22;
}

```

---
### File: src/assets/main.css
---

```css

```

---
### File: src/components/FlowerImage.vue
---

```vue
<script setup lang="ts">
import { computed } from 'vue';
import { GameController } from '@/server/controllers/GameController';
import { FlowerStatus } from '@/shared/types'; // Assure-toi que le chemin est correct

// Définition des props
interface Props {
    slug: string;
    status?: FlowerStatus;
    type?: 'icon' | 'sprite';
    size?: number | string;
    alt?: string;
}

const props = withDefaults(defineProps<Props>(), {
    status: FlowerStatus.MATURE,
    type: 'icon',
    size: 32,
    alt: 'Flower icon'
});

const imageUrl = computed(() => {
    if (!props.slug) return '';
    return GameController.getFlowerAssetUrl(props.slug, props.status, props.type);
});

const sizeStyle = computed(() => {
    const s = props.size;
    const finalSize = typeof s === 'number' ? `${s}px` : s;

    return {
        width: finalSize,
        height: finalSize,
    };
});
</script>

<template>
    <img v-if="imageUrl" :src="imageUrl" :alt="alt" class="flower-image-component pixelated" :style="sizeStyle"
        draggable="false" />
    <div v-else class="flower-image-component pixelated bg-slate-800/50 rounded-md animate-pulse" :style="sizeStyle">
    </div>
</template>

<style scoped>
.flower-image-component {
    object-fit: contain;

    vertical-align: middle;
    display: inline-block;
}

.pixelated {
    image-rendering: pixelated;
    image-rendering: -moz-crisp-edges;
    image-rendering: crisp-edges;
    -ms-interpolation-mode: nearest-neighbor;
}
</style>
```

---
### File: src/components/Footer.vue
---

```vue
<script setup lang="ts">
import { ROUTES_ENUM as routes } from '@/routes/routes_enum'
import ThemeSwitcher from './buttons/ThemeSwitcher.vue'
import DiscordIcon from './icons/DiscordIcon.vue'
import InstagramIcon from './icons/InstagramIcon.vue'

const appTitle = import.meta.env.VITE_APP
const appVersion = import.meta.env.VITE_APP_VERSION

const instagramAccountURL = 'https://instagram.com/comx.app/'
const discordServerURL = 'https://discord.gg/4sJyaynWdW'
</script>

<template>
    <footer class="footer sm:footer-horizontal p-10 bg-slate-950 text-slate-400 border-t border-slate-800">
        <aside>
            <div class="flex items-center gap-2 mb-1">
                <div
                    class="w-6 h-6 bg-emerald-500 rounded flex items-center justify-center text-slate-900 text-xs font-bold shadow-lg shadow-emerald-500/20">
                    B
                </div>
                <span class="text-xl font-bold text-white tracking-tight">{{ appTitle }}</span>
            </div>

            <div class="flex items-center gap-2 mt-1">
                <span class="text-sm">&copy; {{ new Date().getFullYear() }}</span>
                <kbd class="kbd kbd-sm bg-slate-900 border-slate-700 text-emerald-400 font-mono text-xs">
                    v{{ appVersion }}
                </kbd>
            </div>
        </aside>

        <nav>
            <h6 class="footer-title text-white opacity-100 mb-2">Services</h6>
            <a class="link link-hover hover:text-emerald-400 transition-colors">Advertisement</a>
            <a class="link link-hover hover:text-emerald-400 transition-colors">Market API</a>
        </nav>

        <nav>
            <h6 class="footer-title text-white opacity-100 mb-2">Company</h6>
            <RouterLink class="link link-hover hover:text-emerald-400 transition-colors" :to="routes.ABOUT.path">
                About us
            </RouterLink>
            <RouterLink class="link link-hover hover:text-emerald-400 transition-colors" :to="routes.WIKI.path">
                Wiki
            </RouterLink>
            <RouterLink class="link link-hover hover:text-emerald-400 transition-colors" :to="routes.SUPPORT.path">
                Support
            </RouterLink>
        </nav>

        <nav>
            <h6 class="footer-title text-white opacity-100 mb-2">Community</h6>
            <div class="grid grid-flow-col gap-4">
                <a :href="instagramAccountURL" target="_blank"
                    class="hover:text-emerald-400 hover:-translate-y-1 transition-all">
                    <InstagramIcon class="w-6 h-6" />
                </a>
                <a :href="discordServerURL" target="_blank"
                    class="hover:text-emerald-400 hover:-translate-y-1 transition-all">
                    <DiscordIcon class="w-6 h-6" />
                </a>
            </div>
        </nav>
    </footer>
</template>

<style scoped>
/* Optional: Ensure footer links don't have default underlining until hover */
.link {
    text-decoration: none;
}

.link:hover {
    text-decoration: underline;
}
</style>
```

---
### File: src/components/Form.vue
---

```vue
<script setup lang="ts">
import { PropType, Ref } from 'vue'

const props = defineProps({
    method: {
        type: String,
        default: 'POST',
    },
    title: {
        type: String,
        default: 'Form Title',
    },
    submitButtonText: {
        type: String,
        default: 'Submit',
    },
    submitAction: {
        type: Function as PropType<(payload?: any) => void>,
        default: () => {
            console.warn('No submit action provided')
        },
    },
    fieldSetBorder: {
        type: Boolean,
        default: true,
    },
})
</script>

<template>
    <form :method="method" @submit.prevent="submitAction">
        <div class="flex justify-center">
            <fieldset
                class="flex flex-col gap-5 fieldset bg-base-100 rounded-box w-xs phone:w-sm sm:w-md p-6 mt-5 mb-5 text-sm"
                :class="{
                    'border border-base-300': fieldSetBorder,
                }">
                <legend class="fieldset-legend">{{ title }}</legend>

                <h2 v-if="$slots.default" class="color-neutral-content">
                    <slot name="header"></slot>
                </h2>

                <slot name="fields"></slot>

                <div class="flex w-full items-center mt-4">
                    <button class="btn btn-primary rounded-2xl flex-1">{{ submitButtonText }}</button>
                    <slot name="moreBtns"></slot>
                </div>

                <p class="label">
                    <slot name="small"></slot>
                </p>
            </fieldset>
        </div>
    </form>
</template>

```

---
### File: src/components/GlobalModal.vue
---

```vue
<script setup lang="ts">
import { useModalStore } from '@/stores/modal';
import { storeToRefs } from 'pinia';
import { computed } from 'vue';

const modalStore = useModalStore();
const { isOpen, title, message, type, actions, size, component, componentProps, fullscreenSideBarMargin } = storeToRefs(modalStore);

// Configuration visuelle selon le type (couleurs)
const config = computed(() => {
    switch (type.value) {
        case 'success': return { color: 'text-emerald-400', border: 'border-emerald-500/30' };
        case 'error': return { color: 'text-red-400', border: 'border-red-500/30' };
        case 'warning': return { color: 'text-amber-400', border: 'border-amber-500/30' };
        default: return { color: 'text-blue-400', border: 'border-blue-500/30' };
    }
});

// Configuration des tailles (Largeur / Hauteur)
const sizeClasses = computed(() => {
    switch (size.value) {
        case 'large':
            // Idéal pour le Market : Large et occupe 85% de la hauteur
            return 'w-full max-w-6xl h-[85vh]';
        case 'fullscreen':
            return 'w-full h-full max-w-none border-1' + (fullscreenSideBarMargin.value ? ' md:ml-25' : '');
        default:
            // Standard
            return 'w-full max-w-md';
    }
});

// Helper pour le style des boutons
const getBtnClass = (variant?: string) => {
    switch (variant) {
        case 'danger': return 'btn-error text-white';
        case 'ghost': return 'btn-ghost text-slate-400';
        case 'secondary': return 'btn-outline border-slate-600 text-slate-300 hover:bg-slate-700';
        default: return 'btn-primary text-white shadow-lg shadow-emerald-500/20';
    }
};
</script>

<template>
    <transition name="fade">
        <div v-if="isOpen"
            class="fixed inset-0 z-[100] flex items-center justify-center bg-slate-900/80 backdrop-blur-sm p-4"
            @click.self="modalStore.close">

            <transition name="scale">
                <div v-if="isOpen"
                    class="glass-panel flex flex-col p-6 rounded-2xl border shadow-2xl relative overflow-hidden transition-all duration-300"
                    :class="[config.border, sizeClasses]">

                    <div
                        class="absolute -top-10 -right-10 w-32 h-32 bg-white/5 rounded-full blur-3xl pointer-events-none">
                    </div>

                    <div class="flex-none flex items-center gap-4 mb-4">
                        <h3 class="text-xl font-bold tracking-wide" :class="config.color">
                            {{ title }}
                        </h3>
                    </div>

                    <div class="flex-1 overflow-y-auto min-h-0 custom-scrollbar mb-4">

                        <component v-if="component" :is="component" v-bind="componentProps" />

                        <p v-else class="text-slate-300 text-sm leading-relaxed">
                            {{ message }}
                        </p>
                    </div>

                    <div class="flex-none flex justify-end gap-3 border-t border-white/5 pt-4">
                        <button v-for="(action, idx) in actions" :key="idx" @click="action.onClick"
                            class="btn btn-sm rounded-lg font-bold transition-transform hover:scale-105"
                            :class="getBtnClass(action.variant)">
                            {{ action.label }}
                        </button>
                    </div>

                </div>
            </transition>
        </div>
    </transition>
</template>

<style scoped>
.glass-panel {
    background: rgba(15, 23, 42, 0.95);
    /* Légèrement plus opaque pour la lisibilité du Market */
    backdrop-filter: blur(16px);
    box-shadow: 0 0 40px rgba(0, 0, 0, 0.5);
}

/* Scrollbar personnalisée fine et discrète pour le contenu interne */
.custom-scrollbar::-webkit-scrollbar {
    width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 4px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 4px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.3);
}

/* Animations */
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.scale-enter-active,
.scale-leave-active {
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.scale-enter-from,
.scale-leave-to {
    transform: scale(0.95) translateY(10px);
    opacity: 0;
}
</style>
```

---
### File: src/components/Header.vue
---

```vue
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { ROUTES_ENUM as ROUTES } from '@/routes/routes_enum';
import { useAuthModal } from './auth/logic/useAuthModal';
import { RouterLink, useRouter } from 'vue-router';
import { remult } from 'remult'; // Import nécessaire pour vérifier l'utilisateur
import { useAuthStore } from '@/stores/auth';
import { useChatStore } from '@/stores/chat';

const router = useRouter()
const isMenuOpen = ref(false)

const toggleMenu = () => {
    isMenuOpen.value = !isMenuOpen.value
}

const handleLinkClick = (path?: string) => {
    isMenuOpen.value = false;
    if (path) router.push(path);
}

const menuLinks = [
    { name: 'Marketplace', path: ROUTES.MARKET.path },
    { name: 'Wiki', path: ROUTES.WIKI.path },
    { name: 'Leaderboard', path: '#' },
    { name: 'FloraDex', path: ROUTES.FLORADEX.path }
]

const chat = useChatStore()
const auth = useAuthStore()

onMounted(async () => {
    await auth.fetchSessionUser()
})
</script>

<template>
    <nav class="sticky top-0 w-full z-50 bg-slate-900/80 backdrop-blur-md border-b border-slate-700/50">
        <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">

            <button class="flex items-center gap-2 cursor-pointer z-50" @click="handleLinkClick(ROUTES.HOME.path)">
                <div>
                    <img src="/bloomscape_logo.png" alt="Logo" width="45" height="45" />
                </div>
                <span class="font-bold tracking-wide w-40 hidden phone:block">
                    <img src="/bloomscape_text.png" alt="BloomScape">
                </span>
            </button>

            <div class="hidden md:flex gap-8 text-sm font-medium text-slate-400">
                <RouterLink v-for="link in menuLinks" :to="link.path" class="hover:text-white transition-colors">
                    {{ link.name }}
                </RouterLink>
            </div>

            <div class="flex items-center gap-4">

                <div v-if="auth.user" class="dropdown dropdown-end">
                    <label tabindex="0" class="btn btn-ghost btn-circle avatar online placeholder">
                        <div class="w-8 rounded-full ring ring-emerald-500 ring-offset-base-100 ring-offset-2">
                            <img :src="`https://ui-avatars.com/api/?name=${auth.user.tag}&background=10b981&color=fff`"
                                :alt="auth.user.tag" />
                        </div>
                    </label>

                    <ul tabindex="0"
                        class="mt-3 p-2 shadow-lg menu menu-compact dropdown-content bg-slate-800 rounded-box w-52 border border-slate-700 text-slate-200">
                        <li class="menu-title">
                            <span class="text-emerald-400">{{ auth.user.tag }}</span>
                        </li>
                        <li>
                            <RouterLink class="justify-between" :to="ROUTES.CURRENT_USER_PROFILE.path">
                                Profile
                            </RouterLink>
                        </li>

                        <li>
                            <button class="justify-between" @click="chat.toggle">
                                Messages
                            </button>
                        </li>

                        <li v-if="remult.isAllowed('admin')">
                            <RouterLink :to="ROUTES.ADMIN_MANAGER.path">Admin Panel</RouterLink>
                        </li>

                        <div class="divider my-0"></div>

                        <li><a @click="router.push(ROUTES.LOGOUT.path)"
                                class="text-red-400 hover:text-red-300">Logout</a></li>
                    </ul>
                </div>

                <button v-else class="btn btn-sm btn-ghost text-slate-300" @click="() => {
                    const authModal = useAuthModal()
                    authModal.openAuthModal('login')
                }">Login</button>

                <button
                    class="btn btn-sm bg-emerald-500 hover:bg-emerald-400 border-none text-slate-900 font-bold px-6 shadow-lg shadow-emerald-500/20"
                    @click="router.push(ROUTES.LAND.path)">
                    Play
                </button>

                <button @click="toggleMenu" class="md:hidden btn btn-square btn-ghost btn-sm text-slate-300 bg-none">
                    <svg v-if="!isMenuOpen" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                        stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                    </svg>
                    <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
        </div>

        <transition enter-active-class="transition duration-200 ease-out"
            enter-from-class="transform -translate-y-4 opacity-0" enter-to-class="transform translate-y-0 opacity-100"
            leave-active-class="transition duration-150 ease-in" leave-from-class="transform translate-y-0 opacity-100"
            leave-to-class="transform -translate-y-4 opacity-0">
            <div v-if="isMenuOpen" class="md:hidden border-t border-slate-700/50 bg-slate-900/95 backdrop-blur-xl">
                <div class="flex flex-col p-4 space-y-4 text-slate-300 font-medium">
                    <RouterLink v-for="link in menuLinks" :to="link.path"
                        class="block py-2 px-4 rounded-lg hover:bg-slate-800 hover:text-emerald-400 transition-colors"
                        @click="handleLinkClick()">
                        {{ link.name }}
                    </RouterLink>
                </div>
            </div>
        </transition>
    </nav>
</template>
```

---
### File: src/components/HomeMarketTicker.vue
---

```vue
<script setup lang="ts">
import { ref } from 'vue'

const marketTicker = ref([
    { name: 'Moon Rose', change: '+12%', price: 420, up: true },
    { name: 'Sun Sunflower', change: '-2%', price: 85, up: false },
    { name: 'Void Tulip', change: '+5%', price: 1200, up: true },
    { name: 'Basic Daisy', change: '0%', price: 15, up: true },
    { name: 'Crystal Lily', change: '+24%', price: 2400, up: true },
    { name: 'Fire Orchid', change: '-8%', price: 310, up: false },
])
</script>

<template>
    <div class="w-full bg-slate-900/50 border-y border-slate-800 overflow-hidden py-3 backdrop-blur-sm relative z-20">
        <div class="flex gap-12 animate-marquee whitespace-nowrap">
            <div v-for="(item, i) in [...marketTicker, ...marketTicker, ...marketTicker]" :key="i"
                class="flex items-center gap-3 opacity-80 hover:opacity-100 transition-opacity cursor-default">
                <span class="font-bold text-slate-300 text-sm">{{ item.name }}</span>
                <span class="font-mono text-white text-sm">{{ item.price }} S</span>
                <span class="text-xs px-1.5 py-0.5 rounded font-mono"
                    :class="item.up ? 'bg-emerald-500/10 text-emerald-400' : 'bg-red-500/10 text-red-400'">
                    {{ item.change }}
                </span>
                <div class="w-1 h-1 rounded-full bg-slate-700 mx-2"></div>
            </div>
        </div>
    </div>
</template>

<style scoped>
@keyframes marquee {
    0% {
        transform: translateX(0);
    }

    100% {
        transform: translateX(-50%);
    }
}

.animate-marquee {
    animation: marquee 40s linear infinite;
}

.animate-marquee:hover {
    animation-play-state: paused;
}
</style>
```

---
### File: src/components/admin/AdminSideBar.vue
---

```vue
<script setup lang="ts">

// Define the shape of a menu item
export interface MenuItem {
    id: string
    label: string
}

defineProps<{
    activeTab: string
    menuItems: MenuItem[]
}>()

const emit = defineEmits<{
    (e: 'update:tab', id: string): void
}>()
</script>

<template>
    <aside class="w-64 bg-slate-900 border-r border-slate-800 flex flex-col absolute h-full z-10">
        <div class="h-16 flex items-center px-6 border-b border-slate-800 bg-slate-900/50">
            <span class="text-emerald-500 font-bold tracking-wider text-sm uppercase">Admin Managing Tools</span>
        </div>

        <nav class="flex-1 p-4 space-y-1">
            <button v-for="item in menuItems" :key="item.id" @click="emit('update:tab', item.id)"
                class="w-full flex items-center gap-3 px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200"
                :class="activeTab === item.id
                    ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
                    : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'">
                {{ item.label }}
            </button>
        </nav>

        <div class="p-4 border-t border-slate-800 text-xs text-slate-500">
            <p>Admin Panel v1.0</p>
            <p>Server Status: <span class="text-emerald-500">Online</span></p>
        </div>
    </aside>
</template>
```

---
### File: src/components/admin/integrated_views/AdminConfig.vue
---

```vue
<template>
    <div class="space-y-6 max-w-2xl">
        <div class="bg-slate-900 p-6 rounded-xl border border-slate-800">
            <h3 class="font-bold text-white mb-6">Economy Parameters</h3>

            <div class="form-control w-full mb-4">
                <label class="label"><span class="label-text">Global Growth Speed Multiplier</span></label>
                <input type="number" value="1.0" class="input input-bordered bg-slate-950" />
            </div>

            <div class="form-control w-full mb-4">
                <label class="label"><span class="label-text">Market Tax Rate (%)</span></label>
                <input type="number" value="5" class="input input-bordered bg-slate-950" />
            </div>

            <button class="btn btn-primary bg-emerald-600 mt-4">Save Configuration</button>
        </div>
    </div>
</template>
```

---
### File: src/components/admin/integrated_views/AdminDatabase.vue
---

```vue
<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { remult, type Repository, type FieldMetadata, type ClassType } from 'remult'

import { Achievement, ClaimLink, FlowerSpecies, Island, Item, SapPurchase, Tile, User } from '@/shared'

type EntityConfig = {
    label: string
    key: string
    entity: ClassType<any>
}

const ENTITY_MAP: EntityConfig[] = [
    { label: 'Flower Species', key: 'flowers', entity: FlowerSpecies },
    { label: 'Items', key: 'items', entity: Item },
    { label: 'Users', key: 'users', entity: User },
    { label: 'Achievements', key: 'achievements', entity: Achievement },
    { label: 'Islands', key: 'islands', entity: Island },
    { label: 'Tiles', key: 'tiles', entity: Tile },
    { label: 'Sap Purchases', key: 'sap', entity: SapPurchase },
    { label: 'Claim Links', key: 'claimlinks', entity: ClaimLink },
]

const activeEntityKey = ref(ENTITY_MAP[0].key)
const items = ref<any[]>([])
const loading = ref(false)
const error = ref('')

// Pagination State
const page = ref(1)
const pageSize = 100
const totalCount = ref(0)

// Modal State
const showModal = ref(false)
const isEditing = ref(false)
const editingItem = ref<any>({})

// --- 4. COMPUTED HELPERS ---
const currentConfig = computed(() => ENTITY_MAP.find(e => e.key === activeEntityKey.value)!)

// Generic Repo Access
const currentRepo = computed((): Repository<any> => remult.repo(currentConfig.value.entity))

const totalPages = computed(() => Math.ceil(totalCount.value / pageSize))

const displayFields = computed(() => {
    if (!currentRepo.value || !currentRepo.value.metadata) return []
    return currentRepo.value.metadata.fields.toArray().filter(f => !['passwordHash'].includes(f.key))
})

const formFields = computed(() => {
    if (!currentRepo.value || !currentRepo.value.metadata) return []
    return currentRepo.value.metadata.fields.toArray().filter(f =>
        !['createdAt', 'updatedAt', 'passwordHash', 'id'].includes(f.key)
    )
})

// --- 5. ACTIONS ---

async function loadData() {
    loading.value = true
    error.value = ''
    try {
        // 1. Get total count for pagination UI
        totalCount.value = await currentRepo.value.count()

        // 2. Get paginated data
        items.value = await currentRepo.value.find({
            limit: pageSize,
            page: page.value
        })
    } catch (err: any) {
        error.value = err.message
    } finally {
        loading.value = false
    }
}

function changePage(delta: number) {
    const newPage = page.value + delta
    if (newPage > 0 && newPage <= totalPages.value) {
        page.value = newPage
        loadData()
    }
}

// Open Create Modal
function openCreate() {
    isEditing.value = false
    editingItem.value = {}
    showModal.value = true
}

// Open Edit Modal
function openEdit(item: any) {
    isEditing.value = true
    editingItem.value = { ...item }
    showModal.value = true
}

// Save (Create or Update)
async function saveItem() {
    try {
        if (isEditing.value) {
            await currentRepo.value.save(editingItem.value)
        } else {
            await currentRepo.value.insert(editingItem.value)
        }
        await loadData()
        showModal.value = false
    } catch (err: any) {
        alert("Error saving: " + err.message)
    }
}

// Delete
async function deleteItem(item: any) {
    if (!confirm(`Are you sure you want to delete this ${currentConfig.value.label}?`)) return

    try {
        await currentRepo.value.delete(item)
        await loadData()
    } catch (err: any) {
        alert("Error deleting: " + err.message)
    }
}

// Helpers for Inputs
function getInputType(field: FieldMetadata) {
    if (field.valueType === Boolean) return 'checkbox'
    if (field.valueType === Number) return 'number'
    if (field.key.toLowerCase().includes('date') || field.valueType === Date) return 'datetime-local'
    return 'text'
}

function formatDateForInput(date: any) {
    if (!date) return ''
    const d = new Date(date)
    if (isNaN(d.getTime())) return ''
    const offset = d.getTimezoneOffset() * 60000
    return (new Date(d.getTime() - offset)).toISOString().slice(0, 16)
}

// Reset page when tab changes
watch(activeEntityKey, () => {
    page.value = 1
    loadData()
})

onMounted(() => {
    loadData()
})
</script>

<template>
    <div class="h-[calc(100vh-8rem)] flex flex-col">

        <div class="flex flex-wrap gap-2 mb-4 p-1 bg-slate-900 rounded-lg border border-slate-800 w-fit shrink-0">
            <button v-for="conf in ENTITY_MAP" :key="conf.key" @click="activeEntityKey = conf.key"
                class="px-4 py-2 rounded-md text-sm font-medium transition-colors" :class="activeEntityKey === conf.key
                    ? 'bg-emerald-600 text-white shadow-lg'
                    : 'text-slate-400 hover:text-white hover:bg-slate-800'">
                {{ conf.label }}
            </button>
        </div>

        <div
            class="flex justify-between items-center bg-slate-900 p-4 rounded-t-xl border border-slate-800 border-b-0 shrink-0">
            <div>
                <h3 class="font-bold text-white text-lg">{{ currentConfig.label }} Database</h3>
                <p class="text-xs text-slate-500">Manage raw data records directly.</p>
            </div>
            <div class="flex gap-2">
                <button @click="loadData" class="btn btn-sm btn-ghost text-slate-400">Refresh</button>
                <button @click="openCreate"
                    class="btn btn-sm bg-emerald-600 hover:bg-emerald-500 text-white border-none">
                    + New {{ currentConfig.label }}
                </button>
            </div>
        </div>

        <div
            class="flex-1 bg-slate-900 border border-slate-800 rounded-b-xl overflow-scroll flex flex-col min-h-0 relative">

            <div class="overflow-scroll flex-1 custom-scrollbar">

                <div v-if="loading" class="absolute inset-0 flex items-center justify-center bg-slate-900/50 z-20">
                    <span class="loading loading-spinner text-emerald-500 loading-lg"></span>
                </div>

                <div v-if="error" class="p-12 text-center text-red-400">
                    {{ error }}
                </div>

                <div v-else-if="items.length === 0 && !loading"
                    class="h-full flex flex-col items-center justify-center text-slate-500">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-12 h-12 mb-2 opacity-20">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M20.25 7.5l-.625 10.632a2.25 2.25 0 01-2.247 2.118H6.622a2.25 2.25 0 01-2.247-2.118L3.75 7.5m8.25 3.75h3M12 15.75h3M12 12h3m-3 3.75h-3m-3-3.75H9m0 3.75H9m-3-3.75H5.25m3.75 0h-3m3 3.75h-3" />
                    </svg>
                    <p>No data currently available.</p>
                </div>

                <table v-else class="table table-xs w-full">
                    <thead class="bg-slate-950 text-slate-400 sticky top-0 z-10 shadow-sm">
                        <tr>
                            <th class="bg-slate-950 w-24">Actions</th>
                            <th v-for="field in displayFields" :key="field.key" class="bg-slate-950 capitalize">
                                {{ field.caption || field.key }}
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in items" :key="item.id" class="hover:bg-slate-800/50 border-slate-800 group">
                            <td
                                class="flex gap-2 sticky left-0 bg-slate-900 group-hover:bg-slate-800 transition-colors">
                                <button @click="openEdit(item)" class="text-blue-400 hover:text-blue-300">Edit</button>
                                <button @click="deleteItem(item)" class="text-red-400 hover:text-red-300">Del</button>
                            </td>
                            <td v-for="field in displayFields" :key="field.key"
                                class="whitespace-nowrap max-w-xs truncate">
                                <span v-if="field.valueType === Boolean">
                                    <span v-if="item[field.key]" class="text-emerald-400">Yes</span>
                                    <span v-else class="text-slate-600">No</span>
                                </span>
                                <span v-else-if="field.key.toLowerCase().includes('date') || field.valueType === Date"
                                    class="text-slate-500 font-mono text-xs">
                                    {{ item[field.key] ? new Date(item[field.key]).toLocaleString() : '-' }}
                                </span>
                                <span v-else>
                                    {{ item[field.key] }}
                                </span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div
                class="p-2 border-t border-slate-800 text-xs text-slate-400 bg-slate-950 flex justify-between items-center shrink-0">
                <span>Total Records: <span class="text-white">{{ totalCount }}</span></span>

                <div class="flex items-center gap-2">
                    <button @click="changePage(-1)" :disabled="page === 1"
                        class="btn btn-xs btn-ghost disabled:bg-transparent disabled:text-slate-700">
                        « Prev
                    </button>
                    <span class="font-mono">Page {{ page }} / {{ totalPages || 1 }}</span>
                    <button @click="changePage(1)" :disabled="page >= totalPages"
                        class="btn btn-xs btn-ghost disabled:bg-transparent disabled:text-slate-700">
                        Next »
                    </button>
                </div>
            </div>
        </div>

        <div v-if="showModal" class="fixed inset-0 bg-black/80 flex items-center justify-center z-50 backdrop-blur-sm">
            <div
                class="bg-slate-900 border border-slate-700 p-6 rounded-xl w-full max-w-2xl max-h-[90vh] overflow-y-auto shadow-2xl">
                <h3 class="text-xl font-bold text-white mb-6 border-b border-slate-800 pb-2">
                    {{ isEditing ? 'Edit' : 'Create' }} {{ currentConfig.label }}
                </h3>

                <form @submit.prevent="saveItem" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div v-for="field in formFields" :key="field.key" class="form-control">
                        <label class="label py-1">
                            <span class="label-text text-slate-400 text-xs uppercase font-bold">{{ field.caption ||
                                field.key }}</span>
                        </label>

                        <input v-if="getInputType(field) === 'checkbox'" type="checkbox"
                            v-model="editingItem[field.key]"
                            class="checkbox checkbox-primary checkbox-sm border-slate-600" />

                        <input v-else-if="getInputType(field) === 'datetime-local'" type="datetime-local"
                            :value="formatDateForInput(editingItem[field.key])"
                            @input="e => editingItem[field.key] = new Date((e.target as HTMLInputElement).value)"
                            class="input input-sm input-bordered bg-slate-950 border-slate-700 text-slate-200" />

                        <input v-else :type="getInputType(field)" v-model="editingItem[field.key]"
                            class="input input-sm input-bordered bg-slate-900 border-slate-700 text-slate-200 focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500"
                            :placeholder="field.key" />
                    </div>

                    <div class="col-span-full flex justify-end gap-3 mt-6 pt-4 border-t border-slate-800">
                        <button type="button" @click="showModal = false"
                            class="btn btn-ghost text-slate-400">Cancel</button>
                        <button type="submit" class="btn bg-emerald-600 hover:bg-emerald-500 text-white border-none">
                            Save {{ currentConfig.label }}
                        </button>
                    </div>
                </form>
            </div>
        </div>

    </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
    background: #0f172a;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 4px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background: #475569;
}
</style>
```

---
### File: src/components/admin/integrated_views/AdminLogs.vue
---

```vue
<script setup lang="ts">
const recentLogs = [
    { time: '10:42 AM', type: 'WARN', msg: 'High volatility detected on "Void Tulip" market.' },
    { time: '10:38 AM', type: 'INFO', msg: 'User [Pierre] sold 500 Sap worth of items.' },
    { time: '10:15 AM', type: 'ERROR', msg: 'Failed to sync weather service.' },
]
</script>

<template>
    <div class="space-y-4">
        <div class="mockup-code bg-slate-900 text-slate-300 border border-slate-800">
            <pre v-for="(log, i) in recentLogs" :key="i" data-prefix=">">
        <span :class="log.type === 'ERROR' ? 'text-red-400' : log.type === 'WARN' ? 'text-yellow-400' : 'text-emerald-400'">[{{ log.time }}] {{ log.type }}:</span> {{ log.msg }}
      </pre>
        </div>
    </div>
</template>
```

---
### File: src/components/admin/integrated_views/AdminModeration.vue
---

```vue
<template>
    ...
</template>
```

---
### File: src/components/admin/integrated_views/AdminOverview.vue
---

```vue
<template>
    <div class="space-y-6">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div v-for="i in 4" :key="i" class="bg-slate-900 p-6 rounded-xl border border-slate-800">
                <div class="text-slate-500 text-xs uppercase font-bold mb-2">Total Active Users</div>
                <div class="text-3xl font-mono text-white">12,402</div>
                <div class="text-emerald-400 text-xs mt-1">↑ 12% from last week</div>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-6 h-96">
            <div
                class="bg-slate-900 rounded-xl border border-slate-800 flex items-center justify-center text-slate-600">
                [ CHART: Economy Volume (Sap) ]
            </div>
            <div
                class="bg-slate-900 rounded-xl border border-slate-800 flex items-center justify-center text-slate-600">
                [ CHART: New Registrations ]
            </div>
        </div>
    </div>
</template>
```

---
### File: src/components/admin/integrated_views/AdminReports.vue
---

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { remult } from 'remult'
import { UserReport } from '@/shared/analytics/UserReport'
import { ReportStatus, ReportType } from '@/shared'

const repo = remult.repo(UserReport)

const reports = ref<UserReport[]>([])
const loading = ref(false)
const filterStatus = ref<string>('ALL') // 'ALL', 'OPEN', 'RESOLVED'

// Modal state for viewing full details
const selectedReport = ref<UserReport | null>(null)

// --- ACTIONS ---

async function fetchReports() {
    loading.value = true
    try {
        const where: any = {}

        if (filterStatus.value === 'OPEN') {
            where.status = { $in: [ReportStatus.OPEN, ReportStatus.IN_PROGRESS] }
        } else if (filterStatus.value === 'RESOLVED') {
            where.status = { $in: [ReportStatus.RESOLVED, ReportStatus.REJECTED] }
        }

        reports.value = await repo.find({
            where,
            include: { reporter: true },
            orderBy: { createdAt: 'desc' },
            limit: 100
        })
    } catch (e) {
        console.error(e)
    } finally {
        loading.value = false
    }
}

async function updateStatus(report: UserReport, status: string) {
    try {
        await repo.save({ ...report, status: status as any, resolvedAt: new Date() })
        await fetchReports()
        if (selectedReport.value?.id === report.id) selectedReport.value = null // Close modal if open
    } catch (e: any) {
        alert(e.message)
    }
}

// --- HELPERS ---

const getTypeColor = (type: string) => {
    switch (type) {
        case ReportType.BUG: return 'text-red-400 bg-red-500/10 border-red-500/20'
        case ReportType.FEATURE: return 'text-purple-400 bg-purple-500/10 border-purple-500/20'
        case ReportType.PLAYER_REPORT: return 'text-amber-400 bg-amber-500/10 border-amber-500/20'
        default: return 'text-slate-400 bg-slate-500/10 border-slate-500/20'
    }
}

const getStatusBadge = (status: string) => {
    switch (status) {
        case ReportStatus.OPEN: return 'badge-info'
        case ReportStatus.IN_PROGRESS: return 'badge-warning'
        case ReportStatus.RESOLVED: return 'badge-success'
        case ReportStatus.REJECTED: return 'badge-error'
        default: return 'badge-ghost'
    }
}

onMounted(fetchReports)
</script>

<template>
    <div class="h-[calc(100vh-8rem)] flex flex-col">

        <div class="flex justify-between items-center mb-4 bg-slate-900 p-4 rounded-xl border border-slate-800">
            <div class="flex gap-2">
                <button @click="filterStatus = 'ALL'; fetchReports()" class="btn btn-sm"
                    :class="filterStatus === 'ALL' ? 'btn-primary' : 'btn-ghost'">
                    All
                </button>
                <button @click="filterStatus = 'OPEN'; fetchReports()" class="btn btn-sm"
                    :class="filterStatus === 'OPEN' ? 'btn-primary' : 'btn-ghost'">
                    Open / In Progress
                </button>
                <button @click="filterStatus = 'RESOLVED'; fetchReports()" class="btn btn-sm"
                    :class="filterStatus === 'RESOLVED' ? 'btn-primary' : 'btn-ghost'">
                    Archives
                </button>
            </div>
            <button @click="fetchReports" class="btn btn-sm btn-ghost btn-circle">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-5 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 4.992l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
                </svg>
            </button>
        </div>

        <div class="flex-1 bg-slate-900 border border-slate-800 rounded-xl overflow-hidden relative flex flex-col">

            <div v-if="loading"
                class="absolute inset-0 flex items-center justify-center bg-slate-900/50 z-20 backdrop-blur-sm">
                <span class="loading loading-spinner text-emerald-500 loading-lg"></span>
            </div>

            <div class="overflow-y-auto custom-scrollbar flex-1">
                <table class="table table-sm w-full">
                    <thead class="bg-slate-950 text-slate-400 sticky top-0 z-10">
                        <tr>
                            <th>Type</th>
                            <th>Status</th>
                            <th>Subject</th>
                            <th>Reporter</th>
                            <th>Date</th>
                            <th class="text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="report in reports" :key="report.id"
                            class="hover:bg-slate-800/50 border-slate-800 group">

                            <td>
                                <span class="px-2 py-1 rounded text-[10px] font-bold border uppercase tracking-wider"
                                    :class="getTypeColor(report.type)">
                                    {{ report.type }}
                                </span>
                            </td>

                            <td>
                                <div class="badge badge-xs gap-1" :class="getStatusBadge(report.status)">
                                    {{ report.status }}
                                </div>
                            </td>

                            <td class="max-w-xs">
                                <div class="font-bold text-slate-200 truncate">{{ report.title }}</div>
                                <div class="text-xs text-slate-500 truncate">{{ report.description }}</div>
                            </td>

                            <td>
                                <div class="flex items-center gap-2">
                                    <div class="avatar placeholder">
                                        <div class="bg-slate-800 text-slate-400 rounded-full w-6">
                                            <span class="text-xs">{{ report.reporter?.tag.slice(0, 2).toUpperCase()
                                            }}</span>
                                        </div>
                                    </div>
                                    <span class="text-xs font-mono text-slate-400">{{ report.reporter?.tag || 'Unknown'
                                    }}</span>
                                </div>
                            </td>

                            <td class="text-xs font-mono text-slate-500">
                                {{ new Date(report.createdAt!).toLocaleDateString() }}
                            </td>

                            <td class="text-right">
                                <button @click="selectedReport = report" class="btn btn-xs btn-ghost text-emerald-400">
                                    View Details
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>

                <div v-if="reports.length === 0 && !loading" class="p-10 text-center text-slate-500">
                    No reports found for this filter.
                </div>
            </div>
        </div>

        <div v-if="selectedReport"
            class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm"
            @click.self="selectedReport = null">
            <div
                class="bg-slate-900 border border-slate-700 rounded-2xl w-full max-w-2xl shadow-2xl overflow-hidden flex flex-col max-h-[85vh]">

                <div class="p-6 border-b border-slate-800 bg-slate-950 flex justify-between items-start">
                    <div>
                        <div class="flex items-center gap-2 mb-2">
                            <span class="px-2 py-1 rounded text-[10px] font-bold border uppercase"
                                :class="getTypeColor(selectedReport.type)">
                                {{ selectedReport.type }}
                            </span>
                            <span class="text-xs text-slate-500 font-mono">{{ selectedReport.id }}</span>
                        </div>
                        <h2 class="text-xl font-bold text-white">{{ selectedReport.title }}</h2>
                    </div>
                    <button @click="selectedReport = null" class="btn btn-sm btn-circle btn-ghost">✕</button>
                </div>

                <div class="p-6 overflow-y-auto flex-1 text-slate-300 leading-relaxed whitespace-pre-wrap">
                    {{ selectedReport.description }}
                </div>

                <div class="p-6 bg-slate-950 border-t border-slate-800 flex justify-between items-center">
                    <div class="text-xs text-slate-500">
                        Reported by <span class="text-white">{{ selectedReport.reporter?.tag }}</span> on {{ new
                            Date(selectedReport.createdAt!).toLocaleString() }}
                    </div>

                    <div class="flex gap-2"
                        v-if="selectedReport.status === ReportStatus.OPEN || selectedReport.status === ReportStatus.IN_PROGRESS">
                        <button @click="updateStatus(selectedReport, ReportStatus.IN_PROGRESS)"
                            class="btn btn-sm btn-warning btn-outline">
                            Mark In Progress
                        </button>
                        <button @click="updateStatus(selectedReport, ReportStatus.REJECTED)"
                            class="btn btn-sm btn-error btn-outline">
                            Reject
                        </button>
                        <button @click="updateStatus(selectedReport, ReportStatus.RESOLVED)"
                            class="btn btn-sm btn-success">
                            Resolve
                        </button>
                    </div>
                    <div v-else class="badge badge-lg badge-outline">
                        {{ selectedReport.status }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
    width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
    background: #0f172a;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background: #475569;
}
</style>
```

---
### File: src/components/admin/integrated_views/AdminUsers.vue
---

```vue
<script setup lang="ts">
import { ref, onMounted, watch, computed } from 'vue'
import { remult } from 'remult'
import { User } from '@/shared/user/User'
import { Item, FlowerSpecies, Achievement } from '@/shared'
import { AdminController } from '@/server/controllers/AdminController'
import { Role } from '@/shared/types'

// --- REPOSITORIES ---
const userRepo = remult.repo(User)

// --- STATE: LIST ---
const users = ref<User[]>([])
const totalCount = ref(0)
const loading = ref(false)
const searchQuery = ref('')
const page = ref(1)
const pageSize = 20

// --- STATE: DRAWER / ACTIONS ---
const selectedUser = ref<User | null>(null)
const isActionLoading = ref(false)

// --- STATE: BAN MODAL ---
const showBanModal = ref(false)
const banTargetUser = ref<User | null>(null)
const banReason = ref('')

// Catalogs for Dropdowns
const catalogItems = ref<Item[]>([])
const catalogSpecies = ref<FlowerSpecies[]>([])
const catalogAchievements = ref<Achievement[]>([])

// Forms
const giveItemForm = ref({ slug: '', quantity: 1 })
const giveFlowerForm = ref({ slug: '', quality: 0.5 })
const giveAchieveForm = ref({ slug: '' })

// --- FETCHING ---

async function fetchUsers() {
    loading.value = true
    try {
        const where: any = {}
        if (searchQuery.value) {
            where.tag = { $contains: searchQuery.value }
        }

        totalCount.value = await userRepo.count(where)
        users.value = await userRepo.find({
            where,
            limit: pageSize,
            page: page.value,
            orderBy: { createdAt: 'desc' }
        })
    } catch (e) {
        console.error(e)
    } finally {
        loading.value = false
    }
}

async function loadCatalogs() {
    if (catalogItems.value.length > 0) return

    const [items, flowers, ach] = await Promise.all([
        remult.repo(Item).find({ orderBy: { name: 'asc' } }),
        remult.repo(FlowerSpecies).find({ orderBy: { name: 'asc' } }),
        remult.repo(Achievement).find({ orderBy: { name: 'asc' } })
    ])
    catalogItems.value = items
    catalogSpecies.value = flowers
    catalogAchievements.value = ach
}

// --- USER ACTIONS ---

async function openUser(user: User) {
    selectedUser.value = user
    await loadCatalogs()
    if (catalogItems.value.length) giveItemForm.value.slug = catalogItems.value[0].slug
    if (catalogSpecies.value.length) giveFlowerForm.value.slug = catalogSpecies.value[0].slugName
    if (catalogAchievements.value.length) giveAchieveForm.value.slug = catalogAchievements.value[0].slug
}

async function closeUser() {
    selectedUser.value = null
}

// --- BAN LOGIC ---

function openBanModal(user: User) {
    banTargetUser.value = user
    banReason.value = ''
    showBanModal.value = true
}

async function confirmBan() {
    if (!banTargetUser.value || !banReason.value) return
    isActionLoading.value = true

    try {
        const res = await AdminController.banUser(banTargetUser.value.id, banReason.value)
        alert(res.message)
        showBanModal.value = false
        // Refresh list to show ban status if visualized
        await fetchUsers()
        if (selectedUser.value?.id === banTargetUser.value.id) {
            closeUser()
        }
    } catch (e: any) {
        alert(e.message)
    } finally {
        isActionLoading.value = false
    }
}

// --- GIVE LOGIC ---

async function performGiveItem() {
    if (!selectedUser.value) return
    isActionLoading.value = true
    try {
        const res = await AdminController.giveItem(
            selectedUser.value.id,
            giveItemForm.value.slug,
            giveItemForm.value.quantity
        )
        alert(res.message)
    } catch (e: any) {
        alert(e.message)
    } finally {
        isActionLoading.value = false
    }
}

async function performGiveFlower() {
    if (!selectedUser.value) return
    isActionLoading.value = true
    try {
        const res = await AdminController.giveFlower(
            selectedUser.value.id,
            giveFlowerForm.value.slug,
            giveFlowerForm.value.quality
        )
        alert(res.message)
    } catch (e: any) {
        alert(e.message)
    } finally {
        isActionLoading.value = false
    }
}

async function performGiveAchievement() {
    if (!selectedUser.value) return
    isActionLoading.value = true
    try {
        const res = await AdminController.giveAchievement(
            selectedUser.value.id,
            giveAchieveForm.value.slug
        )
        alert(res.message)
    } catch (e: any) {
        alert(e.message)
    } finally {
        isActionLoading.value = false
    }
}

// Watchers
watch([page, searchQuery], () => fetchUsers())
onMounted(fetchUsers)

// Helper
const totalPages = computed(() => Math.ceil(totalCount.value / pageSize) || 1)
</script>

<template>
    <div class="h-[calc(100vh-8rem)] flex flex-col relative">

        <div class="flex justify-between items-center mb-4 bg-slate-900 p-4 rounded-xl border border-slate-800">
            <div class="relative w-96">
                <input v-model.lazy="searchQuery" type="text" placeholder="Search by tag..."
                    class="input input-sm w-full bg-slate-950 border-slate-700 focus:border-emerald-500" />
            </div>
            <div class="flex items-center gap-4 text-sm text-slate-400">
                <span>Total Users: {{ totalCount }}</span>
                <div class="flex gap-2">
                    <button @click="page--" :disabled="page === 1" class="btn btn-xs btn-ghost">«</button>
                    <span>{{ page }} / {{ totalPages }}</span>
                    <button @click="page++" :disabled="page >= totalPages" class="btn btn-xs btn-ghost">»</button>
                </div>
            </div>
        </div>

        <div
            class="flex-1 bg-slate-900 border border-slate-800 rounded-xl overflow-hidden flex flex-col min-h-0 relative">
            <div v-if="loading"
                class="absolute inset-0 z-10 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center">
                <span class="loading loading-spinner text-emerald-500"></span>
            </div>

            <div class="overflow-y-auto custom-scrollbar flex-1">
                <table class="table table-sm w-full">
                    <thead class="bg-slate-950 text-slate-400 sticky top-0 z-10">
                        <tr>
                            <th>User</th>
                            <th>Info</th>
                            <th>Economy</th>
                            <th>Roles</th>
                            <th>Joined</th>
                            <th class="text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="user in users" :key="user.id"
                            class="hover:bg-slate-800/50 border-slate-800 transition-colors group">

                            <td>
                                <div class="flex items-center gap-3">
                                    <div class="avatar placeholder">
                                        <div class="bg-slate-800 text-slate-300 rounded-full w-8">
                                            <span>{{ user.tag.slice(0, 2).toUpperCase() }}</span>
                                        </div>
                                    </div>
                                    <div>
                                        <div class="font-bold flex items-center gap-2">
                                            {{ user.tag }}
                                            <span v-if="user.banned" class="badge badge-xs badge-error">BANNED</span>
                                        </div>
                                        <div class="text-[10px] text-slate-500 font-mono">{{ user.id }}</div>
                                    </div>
                                </div>
                            </td>

                            <td>
                                <div class="flex flex-col text-xs text-slate-400">
                                    <span>Lvl {{ user.level }}</span>
                                    <span>{{ user.xp }} XP</span>
                                </div>
                            </td>

                            <td>
                                <div class="font-mono text-emerald-400">{{ user.sap }} <span
                                        class="text-xs text-slate-500">Sap</span></div>
                            </td>

                            <td>
                                <div class="flex gap-1">
                                    <span v-if="user.roles.includes(Role.ADMIN)"
                                        class="badge badge-error badge-xs text-white">ADMIN</span>
                                    <span v-else class="badge badge-ghost badge-xs">USER</span>
                                </div>
                            </td>

                            <td class="text-xs text-slate-500">
                                {{ new Date(user.createdAt!).toLocaleDateString() }}
                            </td>

                            <td class="text-right">
                                <button @click="openUser(user)" class="btn btn-xs btn-ghost text-blue-400">
                                    Manage
                                </button>
                                <button @click="openBanModal(user)"
                                    class="btn btn-xs btn-ghost text-red-400 opacity-50 hover:opacity-100"
                                    title="Quick Ban">
                                    Ban
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <Transition name="slide">
            <div v-if="selectedUser"
                class="absolute inset-y-0 right-0 w-[500px] bg-slate-900 border-l border-slate-700 shadow-2xl z-20 flex flex-col">

                <div class="p-6 border-b border-slate-800 bg-slate-950 flex justify-between items-start">
                    <div>
                        <h2 class="text-xl font-bold text-white mb-1">Manage User</h2>
                        <p class="text-emerald-400 font-mono text-sm">{{ selectedUser.tag }}</p>
                    </div>
                    <button @click="closeUser" class="btn btn-circle btn-sm btn-ghost">✕</button>
                </div>

                <div class="flex-1 overflow-y-auto p-6 space-y-8 custom-scrollbar">

                    <div class="space-y-4">
                        <h3
                            class="text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-800 pb-2">
                            Moderation Actions
                        </h3>
                        <div class="grid grid-cols-2 gap-3">
                            <button @click="openBanModal(selectedUser)" class="btn btn-outline btn-error btn-sm w-full">
                                Ban User
                            </button>
                            <button class="btn btn-outline btn-warning btn-sm w-full">
                                Warn
                            </button>
                            <button class="btn btn-outline btn-ghost btn-sm w-full col-span-2">
                                View Logs
                            </button>
                        </div>
                    </div>

                    <div class="space-y-4">
                        <h3
                            class="text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-800 pb-2">
                            Give Items
                        </h3>
                        <div class="bg-slate-800/30 p-4 rounded-lg border border-slate-800 space-y-3">
                            <div>
                                <label class="label text-xs">Item</label>
                                <select v-model="giveItemForm.slug"
                                    class="select select-sm w-full bg-slate-900 border-slate-700">
                                    <option v-for="item in catalogItems" :key="item.id" :value="item.slug">
                                        {{ item.name }} ({{ item.type }})
                                    </option>
                                </select>
                            </div>
                            <div class="flex gap-2">
                                <div class="flex-1">
                                    <label class="label text-xs">Amount</label>
                                    <input type="number" v-model="giveItemForm.quantity"
                                        class="input input-sm w-full bg-slate-900 border-slate-700" min="1" />
                                </div>
                                <div class="flex items-end">
                                    <button @click="performGiveItem" :disabled="isActionLoading"
                                        class="btn btn-sm btn-primary">
                                        Give
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="space-y-4">
                        <h3
                            class="text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-800 pb-2">
                            Give Seed/Flower
                        </h3>
                        <div class="bg-slate-800/30 p-4 rounded-lg border border-slate-800 space-y-3">
                            <div>
                                <label class="label text-xs">Species</label>
                                <select v-model="giveFlowerForm.slug"
                                    class="select select-sm w-full bg-slate-900 border-slate-700">
                                    <option v-for="s in catalogSpecies" :key="s.id" :value="s.slugName">
                                        {{ s.name }} ({{ s.rarity }})
                                    </option>
                                </select>
                            </div>
                            <div>
                                <label class="label text-xs">Quality: {{ Math.round(giveFlowerForm.quality * 100)
                                }}%</label>
                                <input type="range" min="0" max="1" step="0.01" v-model.number="giveFlowerForm.quality"
                                    class="range range-xs range-accent" />
                            </div>
                            <button @click="performGiveFlower" :disabled="isActionLoading"
                                class="btn btn-sm btn-accent w-full">
                                Generate Seed
                            </button>
                        </div>
                    </div>

                    <div class="space-y-4">
                        <h3
                            class="text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-800 pb-2">
                            Unlock Achievement
                        </h3>
                        <div class="bg-slate-800/30 p-4 rounded-lg border border-slate-800 flex gap-2">
                            <select v-model="giveAchieveForm.slug"
                                class="select select-sm flex-1 bg-slate-900 border-slate-700">
                                <option v-for="a in catalogAchievements" :key="a.id" :value="a.slug">
                                    {{ a.name }}
                                </option>
                            </select>
                            <button @click="performGiveAchievement" :disabled="isActionLoading"
                                class="btn btn-sm btn-secondary">
                                Unlock
                            </button>
                        </div>
                    </div>

                </div>
            </div>
        </Transition>

        <div v-if="selectedUser" @click="closeUser"
            class="absolute inset-0 z-10 bg-slate-950/60 backdrop-blur-sm transition-opacity">
        </div>

        <div v-if="showBanModal"
            class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm">
            <div class="bg-slate-900 border border-red-500/30 rounded-xl w-full max-w-md shadow-2xl p-6">
                <h3 class="text-xl font-bold text-white mb-2 flex items-center gap-2">
                    <span class="text-red-500">🚫</span> Ban User
                </h3>
                <p class="text-slate-400 text-sm mb-4">
                    Are you sure you want to ban <span class="font-bold text-white">{{ banTargetUser?.tag }}</span>?
                    This action will restrict their access to the game.
                </p>

                <div class="form-control mb-6">
                    <label class="label pt-0">
                        <span class="label-text text-xs uppercase font-bold text-slate-500">Reason</span>
                    </label>
                    <textarea v-model="banReason"
                        class="textarea textarea-bordered bg-slate-950 border-slate-700 focus:border-red-500 w-full"
                        placeholder="Violation of TOS, harassment..."></textarea>
                </div>

                <div class="flex justify-end gap-3">
                    <button @click="showBanModal = false" class="btn btn-sm btn-ghost text-slate-400">Cancel</button>
                    <button @click="confirmBan" :disabled="!banReason || isActionLoading"
                        class="btn btn-sm btn-error text-white">
                        <span v-if="isActionLoading" class="loading loading-spinner"></span>
                        <span v-else>Confirm Ban</span>
                    </button>
                </div>
            </div>
        </div>

    </div>
</template>

<style scoped>
.slide-enter-active,
.slide-leave-active {
    transition: transform 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
    transform: translateX(100%);
}

.custom-scrollbar::-webkit-scrollbar {
    width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
    background: #0f172a;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background: #475569;
}
</style>
```

---
### File: src/components/auth/AuthModal.vue
---

```vue
<script setup lang="ts">
import { reactive, ref, computed, watch, nextTick } from 'vue'
import { useAuthStore } from '@/stores/auth'
import GoogleLoginBtn from '../buttons/GoogleLoginBtn.vue' // Adjust path if needed
import Form from '../Form.vue' // Adjust path if needed

// --- TYPES ---
// Define keys to ensure type safety in v-for loops
interface FieldConfig {
    label: string
    type: string
    placeholder: string
    vmodel: keyof typeof formData
}

// --- PROPS & EMITS ---
const props = defineProps<{
    isOpen: boolean
    mode?: 'login' | 'signup'
}>()

const emit = defineEmits<{
    'update:isOpen': [value: boolean]
    success: [user: any]
}>()

// --- STATE ---
const mode = ref<'login' | 'signup'>(props.mode || 'login')
const auth = useAuthStore()
const dialogRef = ref<HTMLDialogElement>()

// Reactive form data
const formData = reactive({
    tagOrEmail: '',
    rememberMe: false,
    tag: '',
    email: '',
    passwd: '',
    passwdConfirm: '',
})

// Error state
const error = reactive<Record<string, string>>({})

// --- WATCHERS ---

// Control Dialog Visibility
watch(
    () => props.isOpen,
    (newValue) => {
        nextTick(() => {
            if (newValue && dialogRef.value) {
                dialogRef.value.showModal()
            } else if (!newValue && dialogRef.value) {
                dialogRef.value.close()
            }
        })
    },
    { immediate: true },
)

// Reset state when mode changes
watch(mode, () => {
    resetForm()
})

// --- ACTIONS ---

const resetForm = () => {
    // Clear errors
    Object.keys(error).forEach((key) => delete error[key])

    // Clear fields
    formData.tag = ''
    formData.email = ''
    formData.tagOrEmail = ''
    formData.passwd = ''
    formData.passwdConfirm = ''
    formData.rememberMe = false
}

const closeModal = () => {
    emit('update:isOpen', false)
    resetForm()
}

const handleDialogClose = () => {
    closeModal()
}

const switchMode = () => {
    mode.value = mode.value === 'login' ? 'signup' : 'login'
}

// --- API LOGIC ---

const login = async () => {
    error.general = ''
    try {
        await auth.login(
            formData.tagOrEmail.trim(), // Sanitize input
            formData.passwd,
            formData.rememberMe
        )

        emit('success', auth.user)
        closeModal()
    } catch (err: any) {
        handleApiError(err)
    }
}

const signUp = async () => {
    error.general = ''

    // 1. Frontend Validation
    if (formData.passwd !== formData.passwdConfirm) {
        error.passwdConfirm = "Passwords do not match"
        return
    }

    try {
        // 2. API Call
        await auth.signUp(
            formData.tag.toLowerCase().trim(),
            formData.email.toLowerCase().trim(),
            formData.passwd,
            formData.passwdConfirm,
        )

        // 3. Success Handling
        mode.value = 'login'
        formData.tagOrEmail = formData.email // Auto-fill login
        error.general = '✅ Account successfully registered! You can now login.'

    } catch (err: any) {
        handleApiError(err)
    }
}

const handleApiError = (err: any) => {
    const msg = err.message?.toLowerCase() || ''

    if (msg.includes('password')) {
        error.passwd = err.message
        error.passwdConfirm = err.message
    } else if (msg.includes('email')) {
        error.email = err.message
        error.tagOrEmail = err.message
    } else if (msg.includes('tag')) {
        error.tag = err.message
        error.tagOrEmail = err.message
    } else {
        error.general = err.message || 'Unknown error'
    }
}

// --- CONFIGURATION ---

const fields = computed<FieldConfig[]>(() => {
    if (mode.value === 'login') {
        return [
            {
                label: 'Tag or Email',
                type: 'text',
                placeholder: 'bloom-scape1231 or bloom@scape.me',
                vmodel: 'tagOrEmail',
            },
            {
                label: 'Password',
                type: 'password',
                placeholder: 'Keep it a secret!',
                vmodel: 'passwd',
            },
            {
                label: 'Remember Me?',
                type: 'checkbox',
                placeholder: '',
                vmodel: 'rememberMe',
            },
        ]
    } else {
        return [
            { label: 'Tag', type: 'text', placeholder: 'bloomscape-fan.number1', vmodel: 'tag' },
            { label: 'Email', type: 'email', placeholder: 'bloom@scape.me', vmodel: 'email' },
            { label: 'Password', type: 'password', placeholder: 'Create a password', vmodel: 'passwd' },
            {
                label: 'Confirm Password',
                type: 'password',
                placeholder: 'Repeat password',
                vmodel: 'passwdConfirm',
            },
        ]
    }
})

const formConfig = computed(() => {
    return {
        title: mode.value === 'login' ? 'Login' : 'Sign Up',
        submitButtonText: mode.value === 'login' ? 'Login' : 'Sign Up',
        submitAction: mode.value === 'login' ? login : signUp,
    }
})
</script>

<template>
    <dialog ref="dialogRef" class="modal modal-middle" @close="handleDialogClose">
        <div class="modal-box w-11/12 max-w-md p-0">
            <form method="dialog">
                <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
            </form>

            <div class="space-y-4">

                <Form method="POST" :title="formConfig.title" :submitButtonText="formConfig.submitButtonText"
                    :submitAction="formConfig.submitAction" :fieldSetBorder="false">
                    <template #header>
                        <div v-if="mode === 'signup'" class="text-center text-sm opacity-90">
                            You don't have an account yet? Sign up now and join the
                            <span class="font-bold text-primary">BloomScape</span> community!
                        </div>
                    </template>

                    <div v-if="error.general" :class="[
                        'alert text-sm mb-4',
                        error.general.includes('✅') ? 'alert-success' : 'alert-error',
                    ]">
                        <span>{{ error.general }}</span>
                    </div>

                    <template #fields>
                        <div v-for="field in fields" :key="field.vmodel" class="flex gap-2"
                            :class="field.type === 'checkbox' ? 'form-control' : 'form-control w-full flex-col'">
                            <label :class="[
                                'label',
                                field.type === 'checkbox' ? 'cursor-pointer justify-start gap-3' : '',
                            ]">
                                <span class="label-text">{{ field.label }}</span>
                            </label>

                            <input :type="field.type" :class="[
                                field.type === 'checkbox'
                                    ? 'checkbox checkbox-primary'
                                    : 'input input-bordered w-full',
                                error[field.vmodel] && 'input-error',
                            ]" :placeholder="field.type !== 'checkbox' ? field.placeholder : ''"
                                v-model="formData[field.vmodel]" @input="() => delete error[field.vmodel]" />

                            <div v-if="error[field.vmodel]" class="label">
                                <span class="label-text-alt text-error">{{ error[field.vmodel] }}</span>
                            </div>
                        </div>
                    </template>

                    <template #small>
                        <div class="text-center text-sm mt-2">
                            <span v-if="mode === 'login'">
                                Don't have an account?
                                <button type="button" @click="switchMode" class="link link-primary">Sign Up</button>
                            </span>
                            <span v-else>
                                Already have an account?
                                <button type="button" @click="switchMode" class="link link-primary">Login</button>
                            </span>
                        </div>
                    </template>

                    <template #moreBtns v-if="mode === 'login'">
                        <div class="divider text-xs opacity-60">OR</div>
                        <GoogleLoginBtn />
                    </template>
                </Form>
            </div>
        </div>

        <form method="dialog" class="modal-backdrop">
            <button>close</button>
        </form>
    </dialog>
</template>
```

---
### File: src/components/auth/logic/useAuthModal.ts
---

```ts
import { ref } from 'vue'

// Global state for the modal
const isOpen = ref(false)
const mode = ref<'login' | 'signup'>('login')
const onSuccessCallback = ref<((user: any) => void) | null>(null)

export function useAuthModal() {
  /**
   * Opens the authentication modal.
   * @param newMode - 'login' or 'signup'
   * @param onSuccess - Optional callback function to run after successful auth
   */
  function openAuthModal(newMode: 'login' | 'signup' = 'login', onSuccess?: (user: any) => void) {
    mode.value = newMode
    isOpen.value = true
    // Store the callback to be executed later
    onSuccessCallback.value = onSuccess || null
  }

  function closeAuthModal() {
    isOpen.value = false
    onSuccessCallback.value = null
  }

  /**
   * Called by AuthModal.vue upon successful login/signup
   */
  function handleSuccess(user: any) {
    if (onSuccessCallback.value) {
      onSuccessCallback.value(user)
      onSuccessCallback.value = null // Reset after execution
    }
  }

  return {
    isOpen,
    mode,
    openAuthModal,
    closeAuthModal,
    handleSuccess,
  }
}

```

---
### File: src/components/buttons/GoogleLoginBtn.vue
---

```vue
<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { GoogleSignInButton, type CredentialResponse } from 'vue3-google-signin'

const auth = useAuthStore()

const onSuccess = async (response: CredentialResponse) => {
    if (response.credential) {
        try {
            await auth.googleLogin(response.credential)
        } catch (error) {
            console.error(error)
        }
    }
}

const onError = () => {
    console.error('Google Sign-In failed')
}
</script>

<template>
    <GoogleSignInButton @success="onSuccess" @error="onError" theme="light" size="medium" text="signin_with"
        shape="pill" />
</template>
```

---
### File: src/components/buttons/ThemeSwitcher.vue
---

```vue
<script setup lang="ts">
import { useThemeStore } from '@/stores/theme'
import { storeToRefs } from 'pinia'

const themeStore = useThemeStore()
const { theme } = storeToRefs(themeStore)
</script>

<template>
    <label class="toggle text-base-content">
        <input type="checkbox" class="theme-controller" :checked="theme === 'dark'" @change="themeStore.toggle()" />

        <!-- Sun -->
        <svg aria-label="sun" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor">
                <circle cx="12" cy="12" r="4" />
                <path d="M12 2v2" />
                <path d="M12 20v2" />
                <path d="m4.93 4.93 1.41 1.41" />
                <path d="m17.66 17.66 1.41 1.41" />
                <path d="M2 12h2" />
                <path d="M20 12h2" />
                <path d="m6.34 17.66-1.41 1.41" />
                <path d="m19.07 4.93-1.41 1.41" />
            </g>
        </svg>

        <!-- Moon -->
        <svg aria-label="moon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor">
                <path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z" />
            </g>
        </svg>
    </label>
</template>

```

---
### File: src/components/chat/GlobalChatDrawer.vue
---

```vue
<script setup lang="ts">
import { ref, nextTick, watch, onMounted } from 'vue';
import { useChatStore } from '@/stores/chat';
import { useAuthStore } from '@/stores/auth';

const store = useChatStore();
const auth = useAuthStore();
const messageInput = ref('');
const scrollContainer = ref<HTMLElement | null>(null);

onMounted(() => {
    if (auth.user) store.init();
});

watch(() => store.currentMessages.length, async () => {
    await nextTick();
    if (scrollContainer.value) {
        scrollContainer.value.scrollTop = scrollContainer.value.scrollHeight;
    }
});

watch(() => store.searchQuery, () => {
    store.performSearch();
});

const handleSend = () => {
    if (!messageInput.value.trim()) return;
    store.sendMessage(messageInput.value);
    messageInput.value = '';
};

const isMine = (senderId: string) => senderId === auth.user?.id;

const formatTime = (date?: Date | string) => {
    if (!date) return '';
    return new Date(date).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
};
</script>

<template>
    <Teleport to="body">
        <Transition name="fade">
            <div v-if="store.isOpen"
                class="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-[200] md:bg-transparent md:backdrop-blur-none md:pointer-events-none"
                @click="store.toggle">
            </div>
        </Transition>

        <div class="fixed top-0 right-0 h-full w-full md:w-96 bg-slate-900 border-l border-slate-700 shadow-2xl z-[201] transition-transform duration-300 ease-in-out flex flex-col pointer-events-auto"
            :class="store.isOpen ? 'translate-x-0' : 'translate-x-full'">

            <div class="p-4 border-b border-slate-800 flex items-center justify-between bg-slate-950">
                <h2 v-if="!store.activeChatId" class="font-bold text-white flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                    Communications
                </h2>
                <div v-else class="flex items-center gap-3">
                    <button @click="store.closeConversation"
                        class="btn btn-circle btn-ghost btn-xs text-slate-400 hover:text-white">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                            stroke="currentColor" class="w-4 h-4">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                        </svg>
                    </button>
                    <div class="flex items-center gap-2" v-if="store.activeChat?.otherUser">
                        <div
                            class="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center text-xs font-bold text-white shadow-inner border border-slate-700">
                            {{ store.activeChat.otherUser.tag.substring(0, 2).toUpperCase() }}
                        </div>
                        <div>
                            <div class="text-sm font-bold text-white leading-none">
                                {{ store.activeChat.otherUser.tag }}
                            </div>
                            <div class="text-[10px] text-slate-500">Connected</div>
                        </div>
                    </div>
                </div>
                <button @click="store.toggle" class="btn btn-square btn-ghost btn-sm text-slate-400 hover:text-red-400">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>

            <div v-if="!store.activeChatId" class="flex-1 flex flex-col min-h-0">
                <div class="p-4">
                    <div class="relative">
                        <input type="text" v-model="store.searchQuery" placeholder="Search friends or users..."
                            class="input input-sm w-full bg-slate-800 border-slate-700 focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 text-slate-200 pl-9">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-4 h-4 absolute left-3 top-2.5 text-slate-500">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                        </svg>
                    </div>
                </div>

                <div class="flex-1 overflow-y-auto custom-scrollbar p-2 space-y-1">
                    <div v-if="store.filteredChats?.length > 0">
                        <div class="text-[10px] uppercase font-bold text-slate-500 px-2 mb-2">Inbox</div>
                        <div v-for="chat in store.filteredChats" :key="chat.id" @click="store.openChat(chat.id)"
                            class="flex items-center gap-3 p-2 rounded-lg hover:bg-slate-800 cursor-pointer transition-colors group relative">
                            <div class="relative">
                                <div
                                    class="w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold text-white bg-slate-700 shadow-lg border border-slate-600">
                                    {{ chat.otherUser?.tag.substring(0, 2).toUpperCase() || '?' }}
                                </div>
                                <span v-if="chat.hasUnread"
                                    class="absolute -top-1 -right-1 w-3 h-3 bg-emerald-500 border-2 border-slate-900 rounded-full animate-pulse"></span>
                            </div>
                            <div class="flex-1 min-w-0">
                                <div class="flex justify-between items-baseline">
                                    <span
                                        class="text-sm font-bold text-slate-200 group-hover:text-emerald-400 transition-colors">
                                        {{ chat.otherUser?.tag || 'Unknown User' }}
                                    </span>
                                    <span class="text-[10px] text-slate-500">
                                        {{ formatTime(chat.lastMessageAt) }}
                                    </span>
                                </div>
                                <p class="text-xs text-slate-400 truncate"
                                    :class="{ 'font-bold text-white': chat.hasUnread }">
                                    {{ chat.lastMessagePreview || "Start a conversation" }}
                                </p>
                            </div>
                        </div>
                    </div>

                    <div v-if="store.searchQuery && store.globalSearchResults.length > 0"
                        class="mt-4 pt-4 border-t border-slate-800">
                        <div class="text-[10px] uppercase font-bold text-slate-500 px-2 mb-2">New Connections</div>
                        <div v-for="user in store.globalSearchResults" :key="user.id"
                            @click="store.startChatWithUser(user.id)"
                            class="flex items-center gap-3 p-2 rounded-lg hover:bg-slate-800 cursor-pointer transition-colors opacity-75 hover:opacity-100">
                            <div
                                class="w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold text-white bg-slate-700 border border-dashed border-slate-500">
                                {{ user.tag.substring(0, 2).toUpperCase() }}
                            </div>
                            <div>
                                <div class="text-sm font-bold text-slate-300">{{ user.tag }}</div>
                                <div class="text-xs text-emerald-500">Click to say Hi 👋</div>
                            </div>
                        </div>
                    </div>

                    <div v-if="(!store.filteredChats || store.filteredChats.length === 0) && store.globalSearchResults.length === 0"
                        class="text-center py-10 opacity-50">
                        <div class="text-4xl mb-2">📡</div>
                        <p class="text-sm text-slate-500">No signals found.</p>
                        <p class="text-xs text-slate-600 mt-2">Search for a username to start.</p>
                    </div>
                </div>
            </div>

            <div v-else class="flex-1 flex flex-col min-h-0 bg-slate-950/30">
                <div ref="scrollContainer" class="flex-1 overflow-y-auto p-4 space-y-4 custom-scrollbar">
                    <div v-if="store.currentMessages.length === 0" class="text-center py-10 text-slate-500 text-sm">
                        This is the start of your history with
                        <span class="text-emerald-400 font-bold">{{ store.activeChat?.otherUser?.tag }}</span>.
                    </div>
                    <div v-for="msg in store.currentMessages" :key="msg.id" class="flex flex-col"
                        :class="isMine(msg.senderId) ? 'items-end' : 'items-start'">
                        <div class="max-w-[85%] rounded-2xl px-4 py-2 text-sm shadow-sm break-words" :class="isMine(msg.senderId)
                            ? 'bg-emerald-600 text-white rounded-br-none'
                            : 'bg-slate-800 text-slate-200 rounded-bl-none'">
                            {{ msg.content }}
                        </div>
                        <span class="text-[10px] text-slate-600 mt-1 px-1">
                            {{ formatTime(msg.createdAt) }}
                        </span>
                    </div>
                </div>
                <div class="p-3 border-t border-slate-800 bg-slate-900">
                    <form @submit.prevent="handleSend" class="flex gap-2">
                        <input v-model="messageInput" type="text" placeholder="Type a message..."
                            class="input input-sm flex-1 bg-slate-950 border-slate-700 focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 text-slate-200">
                        <button type="submit" class="btn btn-sm btn-primary btn-square"
                            :disabled="!messageInput.trim()">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                                class="w-4 h-4">
                                <path
                                    d="M3.478 2.405a.75.75 0 00-.926.94l2.432 7.905H13.5a.75.75 0 010 1.5H4.984l-2.432 7.905a.75.75 0 00.926.94 60.519 60.519 0 0018.445-8.986.75.75 0 000-1.218A60.517 60.517 0 003.478 2.405z" />
                            </svg>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </Teleport>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.custom-scrollbar::-webkit-scrollbar {
    width: 5px;
}

.custom-scrollbar::-webkit-scrollbar-track {
    background: transparent;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background: #475569;
}
</style>
```

---
### File: src/components/game/LandScene.vue
---

```vue
<script setup lang="ts">
// ---- IMPORTS ---- //
import { onMounted, onUnmounted, ref, watch, computed } from 'vue';
import { useGameStore } from '@/stores/game';
import { storeToRefs } from 'pinia';
import { LandSceneManager } from './logic/LandSceneManager';
import { useAuthStore } from '@/stores/auth';

// ---- PROPS ---- //
const props = withDefaults(defineProps<{
    userId: string,
    quality?: 'low' | 'high',
    tileSize?: number
}>(), {
    quality: 'high',
    tileSize: 2
});

// ---- STATE ---- //
const gameStore = useGameStore();
const { tiles, currentIsland, isLoading, selectedTile } = storeToRefs(gameStore);

// Isolated ref for canvas
const canvasContainerRef = ref<HTMLDivElement | null>(null);
let sceneManager: LandSceneManager | null = null;
const auth = useAuthStore();

// ---- COMPUTED ---- //
const isCurrentUser = computed(() => auth.user?.id === props.userId);
const hasIsland = computed(() => !!currentIsland.value);

// ---- LOGIC ---- //
const initData = async () => {
    if (!props.userId) return;

    await gameStore.fetchIslandData(props.userId);

    if (sceneManager) {
        sceneManager.updateTiles(tiles.value);
    }
};

const handleHover = (x: number, z: number) => {
    if (!hasIsland.value) {
        gameStore.setHoveredTile(null);
        return;
    }

    if (isNaN(x) || isNaN(z)) {
        gameStore.setHoveredTile(null);
        return;
    }

    const existingTile = gameStore.getTileAt(x, z);

    if (gameStore.hoveredTile?.x !== x || gameStore.hoveredTile?.z !== z) {
        gameStore.setHoveredTile({
            x,
            z,
            id: existingTile?.id,
            isOwned: !!existingTile,
            isAdjacentToLand: sceneManager?.isAdjacentToLand(x, z, gameStore.tiles) || false
        });
    }
};

const handleClick = (x: number, z: number) => {
    if (!hasIsland.value) return;

    const isAlreadySelected =
        gameStore.selectedTile &&
        gameStore.selectedTile.x === x &&
        gameStore.selectedTile.z === z;

    if (isAlreadySelected) {
        gameStore.selectTile(null);
        sceneManager?.setSelection(null, null);
    } else {
        const existingTile = gameStore.getTileAt(x, z);

        gameStore.selectTile({
            x,
            z,
            id: existingTile?.id,
            isOwned: !!existingTile,
            isAdjacentToLand: sceneManager?.isAdjacentToLand(x, z, gameStore.tiles) || false
        });
        sceneManager?.setSelection(x, z);
    }
}

const handleStartAdventure = async () => {
    await gameStore.startAdventure();
};

// ---- LIFECYCLE ---- //
onMounted(async () => {
    await auth.fetchSessionUser();

    if (!canvasContainerRef.value) return;

    sceneManager = new LandSceneManager({
        quality: props.quality,
        tileSize: props.tileSize,
        onHover: handleHover,
        onClick: handleClick // Pass the callback
    });

    sceneManager.init(canvasContainerRef.value);

    initData();
});

onUnmounted(() => {
    if (sceneManager) sceneManager.dispose();
});

// ---- WATCHERS ---- //
watch(() => props.userId, async (newId) => {
    if (newId) await initData();
});

watch(tiles, (newTiles) => {
    if (sceneManager) {
        sceneManager.updateTiles(newTiles);
    }
}, { deep: true });

// Sync visual selection if store changes externally
watch(selectedTile, (newVal) => {
    if (!newVal) {
        sceneManager?.setSelection(null, null);
    }
});

</script>

<template>
    <div class="relative w-full h-full bg-slate-900 overflow-hidden">

        <div ref="canvasContainerRef" class="absolute inset-0 z-0 block"></div>

        <transition name="fade">
            <div v-if="!isLoading && !hasIsland"
                class="absolute inset-0 flex flex-col items-center justify-center bg-slate-900/60 backdrop-blur-sm z-40">

                <div class="card w-96 glass shadow-2xl border border-slate-700">
                    <div class="card-body text-center">
                        <div v-if="isCurrentUser">
                            <h2 class="card-title justify-center text-emerald-400">Get Started!</h2>
                            <p class="text-slate-300">Your BloomScape adventure starts here. Claim your island to start
                                building.</p>
                            <div class="card-actions justify-center mt-4">
                                <button @click="handleStartAdventure"
                                    class="btn btn-primary btn-soft rounded-2xl text-white relative z-50">
                                    Start
                                </button>
                            </div>
                        </div>
                        <div v-else>
                            <h2 class="card-title justify-center text-slate-400">Uncharted Island</h2>
                            <p class="text-slate-500">This player has not started their adventure yet.</p>
                        </div>
                    </div>
                </div>
            </div>
        </transition>

        <div v-if="isLoading"
            class="absolute inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur">
            <span class="loading loading-ring loading-lg text-emerald-500"></span>
        </div>
    </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.slide-up-enter-active,
.slide-up-leave-active {
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.slide-up-enter-from,
.slide-up-leave-to {
    transform: translateY(20px);
    opacity: 0;
}
</style>
```

---
### File: src/components/game/SideBar.vue
---

```vue
<script setup lang="ts">
import { GameController } from '@/server/controllers/GameController';
import { useAuthStore } from '@/stores/auth';
import { useUIStore } from '@/stores/ui';
import { computed, onMounted, ref, Teleport } from 'vue';

import HomeIcon from '../icons/navbar/HomeIcon.vue';
import MarketIcon from '../icons/navbar/MarketIcon.vue';
import InventoryIcon from '../icons/navbar/InventoryIcon.vue';
import SettingsIcon from '../icons/navbar/SettingsIcon.vue';
import { ROUTES_ENUM as ROUTES } from '@/routes/routes_enum';
import { useModalStore } from '@/stores/modal';
import { router } from '@/routes';
import MarketInModal from './modal_features/MarketInModal.vue';
import InventoryInModal from './modal_features/InventoryInModal.vue';

const uiStore = useUIStore();

const auth = useAuthStore();
const userBalance = computed(() => auth.user?.sap ?? 0);

const navigationArray = [
    { name: 'Home', icon: HomeIcon, link: ROUTES.HOME.path },
    {
        name: 'Market', icon: MarketIcon,
        action: async () => {
            const modal = useModalStore();
            modal.open({
                title: 'Marketplace',
                component: MarketInModal,
                size: 'fullscreen',
                path: ROUTES.MARKET.path,
                fullscreenSideBarMargin: true,
            });
        }
    },
    {
        name: 'Inventory', icon: InventoryIcon,
        action: () => {
            const modal = useModalStore();
            modal.open({
                title: 'Inventory',
                component: InventoryInModal,
                size: 'fullscreen',
                path: ROUTES.INVENTORY.path,
                fullscreenSideBarMargin: true,
            })
        }
    },
    { name: 'Settings', icon: SettingsIcon, link: ROUTES.SETTINGS.pathDyn(auth.user?.tag) },
];

onMounted(async () => {
    await auth.fetchSessionUser();
})
</script>

<template>
    <teleport to="body">
        <aside
            class="fixed top-5 left-5 h-[calc(100%-40px)] transition-all duration-300 ease-in-out glass-panel border-r border-white/10 flex flex-col z-[101] pointer-events-auto rounded-2xl overflow-hidden isolate"
            :class="[
                uiStore.isSidebarOpen ? 'w-64 translate-x-0' : 'w-0 -translate-x-full md:w-20 md:translate-x-0'
            ]" @mouseenter="uiStore.isSidebarHovered = true" @mouseleave="uiStore.isSidebarHovered = false"
            @click="uiStore.toggleSidebar">

            <button
                class="h-20 flex items-center border-b border-white/5 relative transition-all duration-300 cursor-pointer"
                :class="uiStore.isSidebarOpen ? 'px-6' : 'justify-center px-0'"
                @click.prevent="router.push(ROUTES.HOME.path)">

                <div>
                    <img src="/bloomscape_logo.png" alt="Logo" width="50" height="50" />
                </div>

                <transition name="fade">
                    <span v-if="uiStore.isSidebarOpen" class="absolute left-20 font-bold tracking-wide w-40">
                        <img src="/bloomscape_text.png" alt="BloomScape">
                    </span>
                </transition>
            </button>

            <nav class="flex-1 py-6 px-3 flex flex-col gap-2">
                <a v-for="(item, index) in navigationArray" :key="index" :href="!item.action ? (item.link || '#') : '#'"
                    @click.stop="() => {
                        if (item.action) item.action()
                    }"
                    class="group flex items-center p-3 rounded-lg transition-all duration-300 hover:bg-white/5 text-gray-400 hover:text-white relative overflow-hidden"
                    :class="uiStore.isSidebarOpen ? '' : 'justify-center'">
                    <div class="w-6 h-6 shrink-0 transition-transform duration-300">
                        <component v-if="item.icon" :is="item.icon" />
                        <div v-else class="w-6 h-6 bg-white/10 rounded-lg"></div>
                    </div>

                    <div class="overflow-hidden transition-all duration-300 ease-in-out"
                        :class="uiStore.isSidebarOpen ? 'max-w-[150px] opacity-100 ml-4' : 'max-w-0 opacity-0 ml-0'">
                        <span class="whitespace-nowrap font-medium">
                            {{ item.name }}
                        </span>
                    </div>
                </a>
            </nav>

            <div class="p-4 mt-auto border-t border-white/5 overflow-hidden transition-all duration-300"
                :class="uiStore.isSidebarOpen ? 'opacity-100 max-h-32' : 'opacity-0 max-h-0 py-0'">
                <div class="bg-slate-800/50 rounded-lg p-3 overflow-hidden">
                    <p class="text-[10px] text-gray-500 uppercase font-bold tracking-wider mb-1">Balance</p>
                    <div class="flex items-center gap-2 text-emerald-400 font-mono text-sm md:text-lg">
                        <span>⟠</span>
                        <span>{{ userBalance }}</span>
                    </div>
                </div>
            </div>
        </aside>
    </teleport>

</template>

<style scoped>
.glass-panel {
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(12px);
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
```

---
### File: src/components/game/TopBar.vue
---

```vue
<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue';
import { remult } from 'remult';
import { useUIStore } from '@/stores/ui';
import { User } from '@/shared';
import { UserController } from '@/server/controllers/UserController';
import { ROUTES_ENUM as ROUTES } from '@/routes/routes_enum';
import { useChatStore } from '@/stores/chat';

// --- PROPS ---
const props = defineProps<{
    userTag: string
}>();

const chat = useChatStore()

// --- STATE ---
const displayedUser = ref<User | null>(null);
const isLoading = ref(true);

// --- COMPUTED ---
// Génère un avatar cohérent basé sur le Tag de l'utilisateur
const avatarUrl = computed(() => {
    const seed = displayedUser.value?.tag || 'default';
    return `https://api.dicebear.com/7.x/avataaars/svg?seed=${seed}&backgroundColor=b6e3f4`;
});

// Simule un nom de secteur basé sur l'ID (Juste pour le lore, ou à remplacer par une vraie data plus tard)
const sectorName = computed(() => {
    if (!displayedUser.value) return 'Unknown';
    const idSlice = displayedUser.value.id.slice(0, 4).toUpperCase();
    return `SEC-${idSlice}`;
});

// --- METHODS ---
const fetchUserData = async () => {
    if (!props.userTag) return;

    isLoading.value = true;
    try {
        const { user } = await UserController.getUserByTag(props.userTag);
        displayedUser.value = user || null;
    } finally {
        isLoading.value = false;
    }
};

// --- LIFECYCLE ---
onMounted(() => {
    fetchUserData();
});

// Recharge si l'ID change (navigation entre profils)
watch(() => props.userTag, () => {
    fetchUserData();
});
</script>

<template>
    <div class="absolute top-0 left-0 w-full p-4 pointer-events-none flex justify-center md:justify-end md:pr-8">

        <div
            class="pointer-events-auto glass-panel rounded-full px-6 py-2 flex items-center gap-6 shadow-2xl shadow-black/40 mt-12 md:mt-2 transition-all duration-300">

            <div class="hidden sm:flex flex-col text-right min-w-[80px]">
                <span class="text-[10px] text-gray-500 uppercase tracking-widest font-bold">Sector</span>

                <span v-if="!isLoading" class="text-sm font-bold text-gray-200 animate-pulse-once">
                    {{ sectorName }}
                </span>
                <div v-else class="h-4 w-16 bg-white/10 rounded animate-pulse mt-1 ml-auto"></div>
            </div>

            <div class="h-8 w-px bg-white/10 hidden sm:block"></div>

            <div class="flex items-center gap-2">
                <div class="tooltip tooltip-bottom" data-tip="Messages">
                    <button class="btn btn-sm btn-circle btn-ghost text-gray-400 hover:text-white hover:bg-white/10"
                        @click="chat.toggle">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                        </svg>
                    </button>
                </div>
            </div>

            <div class="h-8 w-px bg-white/10"></div>

            <div class="flex items-center gap-3 cursor-pointer group">
                <div class="text-right hidden md:block min-w-[80px]">
                    <div v-if="!isLoading"
                        class="text-xs font-bold text-gray-200 group-hover:text-emerald-400 transition-colors">
                        <RouterLink :to="ROUTES.USER_PROFILE.pathDyn(displayedUser?.tag)">
                            {{ displayedUser?.tag || 'Unknown' }}
                        </RouterLink>
                    </div>
                    <div v-else class="h-3 w-20 bg-white/10 rounded animate-pulse mb-1 ml-auto"></div>

                    <div v-if="!isLoading" class="text-[10px] text-gray-500">
                        Level {{ displayedUser?.level || 1 }}
                    </div>
                    <div v-else class="h-2 w-10 bg-white/10 rounded animate-pulse ml-auto"></div>
                </div>

                <div class="avatar" :class="{ 'online': !isLoading }">
                    <div
                        class="w-9 rounded-full ring ring-emerald-500 ring-offset-slate-900 ring-offset-2 bg-slate-800">
                        <img v-if="!isLoading" :src="avatarUrl" alt="Avatar" class="transition-opacity duration-500" />
                        <div v-else class="w-full h-full bg-slate-700 animate-pulse"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.glass-panel {
    background: rgba(30, 41, 59, 0.75);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-5px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-pulse-once {
    animation: fadeIn 0.5s ease-out forwards;
}
</style>
```

---
### File: src/components/game/config/ItemRegistery.ts
---

```ts
import * as THREE from 'three'

export interface ItemConfig {
  id: string
  geometry: THREE.BufferGeometry
  material: THREE.Material
  yOffset: number // To adjust if the model anchor is center or bottom
  scale: number
}

// Reusable geometries/materials to save memory
const geoTree = new THREE.ConeGeometry(0.3, 1, 8)
const matTree = new THREE.MeshStandardMaterial({ color: 0x2d6a4f, flatShading: true })

const geoRock = new THREE.DodecahedronGeometry(0.3)
const matRock = new THREE.MeshStandardMaterial({ color: 0x8d99ae, flatShading: true })

export const ITEM_REGISTRY: Record<string, ItemConfig> = {
  tree_pine: {
    id: 'tree_pine',
    geometry: geoTree,
    material: matTree,
    yOffset: 0.5, // Shift up so base is on ground
    scale: 1,
  },
  rock_small: {
    id: 'rock_small',
    geometry: geoRock,
    material: matRock,
    yOffset: 0.15,
    scale: 1,
  },
}

```

---
### File: src/components/game/logic/AutoTilingUtils.ts
---

```ts
// 1 = North, 2 = East, 4 = South, 8 = West

import { TileData } from './LandSceneManager'

// Summing these gives a unique number from 0 to 15
export interface TileLayout {
  type: 'center' | 'edge' | 'corner' | 'tip' | 'island'
  rotation: number // in Radians
}

export const getTileLayout = (
  x: number,
  z: number,
  tileSize: number,
  allTiles: TileData[],
): TileLayout => {
  // Helper to check if a neighbor exists
  const has = (dx: number, dz: number) => allTiles.some((t) => t.x === x + dx && t.z === z + dz)

  // Calculate Bitmask
  let mask = 0
  if (has(0, tileSize)) mask += 1 // North
  if (has(tileSize, 0)) mask += 2 // East
  if (has(0, -tileSize)) mask += 4 // South
  if (has(-tileSize, 0)) mask += 8 // West

  const PI = Math.PI
  const hPI = Math.PI / 2

  // Lookup Table: Map mask to Shape + Rotation
  switch (mask) {
    // --- CENTER (Surrounded) ---
    case 15:
      return { type: 'center', rotation: 0 }

    // --- EDGES (3 Neighbors) ---
    case 14:
      return { type: 'edge', rotation: PI } // N-E-S (Missing West)
    case 13:
      return { type: 'edge', rotation: -hPI } // N-E-W (Missing South)
    case 11:
      return { type: 'edge', rotation: 0 } // N-S-W (Missing East)
    case 7:
      return { type: 'edge', rotation: hPI } // E-S-W (Missing North)

    // --- CORNERS (2 Neighbors) ---
    case 12:
      return { type: 'corner', rotation: 0 } // S-W (Corner is NE)
    case 6:
      return { type: 'corner', rotation: -hPI } // E-S (Corner is NW)
    case 3:
      return { type: 'corner', rotation: PI } // N-E (Corner is SW)
    case 9:
      return { type: 'corner', rotation: hPI } // N-W (Corner is SE)

    // --- TIPS (1 Neighbor) - Optional, can reuse corner or edge ---
    // For simplicity, let's treat tips like corners or define a specific logic
    case 8:
      return { type: 'corner', rotation: hPI }
    case 4:
      return { type: 'corner', rotation: 0 }
    case 2:
      return { type: 'corner', rotation: -hPI }
    case 1:
      return { type: 'corner', rotation: PI }

    // --- ISLAND (0 Neighbors) ---
    case 0:
      return { type: 'center', rotation: 0 } // Or specific single island mesh

    default:
      return { type: 'center', rotation: 0 } // Fallback
  }
}

```

---
### File: src/components/game/logic/LandSceneManager.ts
---

```ts
// ---- IMPORTS ---- //
import * as THREE from 'three'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js'
import { WorldElementManager } from './WorldElementsManager'
import { getTileLayout } from './AutoTilingUtils'

// ---- CONFIGURATION GLOBALE ---- //
const WORLD_SIZE = 60 // Taille de la grille scannée pour générer l'eau (60x60 = 3600 tuiles)
const WATER_ANIM_SPEED = 300

const COLORS = {
  highlight: 0x333399,
  selection: 0x3333cc,
  owned: 0x10b981,
  grid: 0xffffff,
  waterBase: 0xffffff, // Blanc pour garder la couleur originale des sprites
}

// ---- TYPES ---- //
export interface SceneConfig {
  quality: 'low' | 'high'
  tileSize: number
  onHover: (x: number, z: number) => void
  onClick?: (x: number, z: number) => void
}

export interface TileData {
  x: number
  z: number
  flowerId?: string
}

// Les 5 catégories de textures d'eau
type WaterCategory = 'open' | '1side' | '2sides' | '3sides' | '4sides'

// ---- CLASS DEFINITION ---- //
export class LandSceneManager {
  private scene!: THREE.Scene
  private camera!: THREE.OrthographicCamera
  private renderer!: THREE.WebGLRenderer
  private controls!: OrbitControls
  private raycaster: THREE.Raycaster
  private mouse: THREE.Vector2
  private animationId: number = 0

  private elementManager: WorldElementManager

  // Objets utilitaires
  private cursorMesh!: THREE.Mesh
  private selectionMesh!: THREE.Object3D
  // Un plan invisible pour capter la souris sur l'eau (car l'eau est faite de plein de petits bouts)
  private raycastPlane!: THREE.Mesh

  // --- GESTION EAU ---
  // Stockage des textures chargées : { 'open': [Texture, Texture...], ... }
  private waterTextureSets: Record<WaterCategory, THREE.Texture[]> = {
    open: [],
    '1side': [],
    '2sides': [],
    '3sides': [],
    '4sides': [],
  }

  // Stockage des Meshs Instanciés (1 par catégorie)
  private waterMeshes: Record<WaterCategory, THREE.InstancedMesh | null> = {
    open: null,
    '1side': null,
    '2sides': null,
    '3sides': null,
    '4sides': null,
  }

  private currentWaterFrame: number = 0
  private lastWaterUpdate: number = 0
  // -------------------

  // Meshs Terre
  private meshCenter!: THREE.InstancedMesh
  private meshEdge!: THREE.InstancedMesh
  private meshCorner!: THREE.InstancedMesh

  private onDownPosition = new THREE.Vector2()
  private container: HTMLElement | null = null
  private config: SceneConfig

  constructor(config: SceneConfig) {
    this.config = config
    this.raycaster = new THREE.Raycaster()
    this.mouse = new THREE.Vector2()

    // Binding des méthodes
    this.onMouseMove = this.onMouseMove.bind(this)
    this.onMouseClick = this.onMouseClick.bind(this)
    this.onWindowResize = this.onWindowResize.bind(this)
    this.onMouseDown = this.onMouseDown.bind(this)
  }

  // ---- INITIALIZATION ---- //
  public init(container: HTMLElement) {
    this.container = container

    // Nettoyage du conteneur
    while (this.container.firstChild) {
      this.container.removeChild(this.container.firstChild)
    }

    const width = this.container.clientWidth
    const height = this.container.clientHeight

    // 1. Scene
    this.scene = new THREE.Scene()
    this.scene.background = new THREE.Color(0x87ceeb)

    // 2. Lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 1.5)
    this.scene.add(ambientLight)

    const dirLight = new THREE.DirectionalLight(0xfff7ed, 3.0)
    dirLight.position.set(50, 80, 40)
    dirLight.castShadow = true
    this.scene.add(dirLight)

    // 3. Camera (Iso)
    const aspect = width / height
    const frustumSize = 40
    this.camera = new THREE.OrthographicCamera(
      (frustumSize * aspect) / -2,
      (frustumSize * aspect) / 2,
      frustumSize / 2,
      frustumSize / -2,
      1,
      1000,
    )
    this.camera.position.set(40, 40, 40)
    this.camera.lookAt(0, 0, 0)
    this.camera.zoom = 4.5

    // 4. Renderer
    this.renderer = new THREE.WebGLRenderer({
      antialias: this.config.quality === 'high',
      alpha: false,
      logarithmicDepthBuffer: true,
    })
    this.renderer.setSize(width, height)
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
    this.renderer.shadowMap.enabled = true
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping
    this.container.appendChild(this.renderer.domElement)

    // 5. Controls
    this.controls = new OrbitControls(this.camera, this.renderer.domElement)
    this.controls.enableDamping = true
    this.controls.dampingFactor = 0.05
    this.controls.minZoom = 0.5
    this.controls.maxZoom = 4
    this.controls.enableRotate = false
    this.controls.enablePan = true
    this.controls.screenSpacePanning = true
    this.controls.minPolarAngle = Math.PI / 3 - 0.05
    this.controls.maxPolarAngle = Math.PI / 3 + 0.05
    this.controls.touches = { ONE: THREE.TOUCH.PAN, TWO: THREE.TOUCH.DOLLY_PAN }
    this.controls.mouseButtons = { LEFT: THREE.MOUSE.PAN, MIDDLE: THREE.MOUSE.DOLLY, RIGHT: null }

    this.createWorld()

    this.elementManager = new WorldElementManager(this.scene)

    this.addEventListeners()
    this.animate()
  }

  // ---- WORLD GENERATION ---- //
  private createWorld() {
    const { tileSize } = this.config
    const loader = new THREE.TextureLoader()

    // --- 1. CHARGEMENT DES TEXTURES D'EAU (15 FRAMES PAR CATÉGORIE) ---
    const loadFrames = (folder: string): THREE.Texture[] => {
      const frames: THREE.Texture[] = []
      for (let i = 1; i <= 16; i++) {
        // Chemin attendu : /textures/water/open/frame1.png
        const path = `/textures/water/${folder}/frame${i}.png`
        const tex = loader.load(path)
        tex.magFilter = THREE.NearestFilter
        tex.minFilter = THREE.NearestFilter
        tex.colorSpace = THREE.SRGBColorSpace
        frames.push(tex)
      }
      return frames
    }

    // Charger les 5 sets
    this.waterTextureSets.open = loadFrames('open')
    this.waterTextureSets['1side'] = loadFrames('1side')
    this.waterTextureSets['2sides'] = loadFrames('2sides')
    this.waterTextureSets['3sides'] = loadFrames('3sides')
    this.waterTextureSets['4sides'] = loadFrames('4sides')

    // --- 2. CRÉATION DES INSTANCED MESHES EAU ---
    const waterGeo = new THREE.PlaneGeometry(tileSize, tileSize)

    const createWaterMesh = (category: WaterCategory) => {
      const initialMap = this.waterTextureSets[category][0] || null
      const mat = new THREE.MeshStandardMaterial({
        map: initialMap,
        color: COLORS.waterBase,
        roughness: 0.1,
        metalness: 0.1,
        transparent: true,
        opacity: 0.4,
        side: THREE.DoubleSide,
      })

      // On prévoit large pour le buffer (4000 tuiles max)
      const mesh = new THREE.InstancedMesh(waterGeo, mat, 4000)
      mesh.receiveShadow = true
      mesh.count = 0 // Initialement vide
      this.scene.add(mesh)
      return mesh
    }

    this.waterMeshes.open = createWaterMesh('open')
    this.waterMeshes['1side'] = createWaterMesh('1side')
    this.waterMeshes['2sides'] = createWaterMesh('2sides')
    this.waterMeshes['3sides'] = createWaterMesh('3sides')
    this.waterMeshes['4sides'] = createWaterMesh('4sides')

    // --- 3. PLAN DE RAYCASTING (INVISIBLE) ---
    // Remplace le sol physique pour la détection de la souris
    const raycastGeo = new THREE.PlaneGeometry(WORLD_SIZE * tileSize * 2, WORLD_SIZE * tileSize * 2)
    const raycastMat = new THREE.MeshBasicMaterial({ visible: false })
    this.raycastPlane = new THREE.Mesh(raycastGeo, raycastMat)
    this.raycastPlane.rotation.x = -Math.PI / 2
    this.scene.add(this.raycastPlane)

    // --- 4. GRID HELPER ---
    const totalSize = WORLD_SIZE * tileSize
    const gridHelper = new THREE.GridHelper(totalSize, WORLD_SIZE, COLORS.grid, COLORS.grid)
    gridHelper.position.set(tileSize / 2, 0.05, tileSize / 2)
    gridHelper.material.opacity = 0.15
    gridHelper.material.transparent = true
    this.scene.add(gridHelper)

    const cursorGeo = new THREE.PlaneGeometry(tileSize, tileSize)
    const cursorMat = new THREE.MeshBasicMaterial({
      color: COLORS.highlight,
      transparent: true,
      opacity: 0.5,
      side: THREE.DoubleSide,
    })
    this.cursorMesh = new THREE.Mesh(cursorGeo, cursorMat)
    this.cursorMesh.rotation.x = -Math.PI / 2
    this.cursorMesh.visible = false
    this.scene.add(this.cursorMesh)

    // --- 5. CURSOR & SELECTION ---
    const boxGeo = new THREE.BoxGeometry(tileSize, 0.55, tileSize)

    // 2. On génère uniquement les arêtes (les lignes) de cette boîte
    const edges = new THREE.EdgesGeometry(boxGeo)

    // 3. On crée l'objet Ligne
    this.selectionMesh = new THREE.LineSegments(
      edges,
      new THREE.LineBasicMaterial({
        color: 0xffff00, // Jaune vif pour bien voir la sélection (ou COLORS.selection)
        linewidth: 2,
      }),
    )

    this.selectionMesh.visible = false
    this.scene.add(this.selectionMesh)

    // --- 6. LAND MESHES (TERRE) ---
    const setupTex = (url: string) => {
      const tex = loader.load(url)
      tex.magFilter = THREE.NearestFilter
      tex.minFilter = THREE.NearestFilter
      tex.colorSpace = THREE.SRGBColorSpace
      return tex
    }

    const texCenter = setupTex('/textures/soil_center.png')
    const texEdge = setupTex('/textures/soil_edge.png')
    const texCorner = setupTex('/textures/soil_corner.png')
    const texSideGrass = setupTex('/textures/land_grass_side.png')
    const texSideDirt = setupTex('/textures/soil_center.png')
    const texBottomRock = setupTex('/textures/land_bottom.png')

    const matSettings = { color: 0xffffff, roughness: 1.0, metalness: 0.0 }
    // (Materials setup shortcut for brevity - same as your original code)
    const matSideDirt = new THREE.MeshStandardMaterial({ map: texSideDirt, ...matSettings })
    const matSideGrass = new THREE.MeshStandardMaterial({ map: texSideGrass, ...matSettings })
    const matBottom = new THREE.MeshStandardMaterial({ map: texBottomRock, ...matSettings })
    const matTopCenter = new THREE.MeshStandardMaterial({ map: texCenter, ...matSettings })
    const matTopEdge = new THREE.MeshStandardMaterial({ map: texEdge, ...matSettings })
    const matTopCorner = new THREE.MeshStandardMaterial({ map: texCorner, ...matSettings })

    const matsCenter = [matSideDirt, matSideDirt, matTopCenter, matBottom, matSideDirt, matSideDirt]
    const matsEdge = [matSideDirt, matSideDirt, matTopEdge, matBottom, matSideDirt, matSideGrass]
    const matsCorner = [
      matSideGrass,
      matSideDirt,
      matTopCorner,
      matBottom,
      matSideGrass,
      matSideDirt,
    ]

    const geo = new THREE.BoxGeometry(this.config.tileSize * 0.97, 0.5, this.config.tileSize * 0.97)

    this.meshCenter = new THREE.InstancedMesh(geo, matsCenter as any, 2000)
    this.meshEdge = new THREE.InstancedMesh(geo, matsEdge as any, 2000)
    this.meshCorner = new THREE.InstancedMesh(geo, matsCorner as any, 2000)

    this.scene.add(this.meshCenter)
    this.scene.add(this.meshEdge)
    this.scene.add(this.meshCorner)
    ;[this.meshCenter, this.meshEdge, this.meshCorner].forEach((m) => {
      m.receiveShadow = true
      m.castShadow = true
      m.count = 0
    })
  }

  // ---- DATA BINDING & UPDATE LOGIC ---- //
  public updateTiles(landTiles: TileData[]) {
    const { tileSize } = this.config

    // --- ETAPE 1 : UPDATE TERRE ---
    let countCenter = 0,
      countEdge = 0,
      countCorner = 0
    const dummy = new THREE.Object3D()

    // On crée un Set pour vérifier rapidement si une case est de la terre
    const landSet = new Set<string>()
    landTiles.forEach((t) => landSet.add(`${t.x},${t.z}`))

    landTiles.forEach((tile) => {
      const layout = getTileLayout(tile.x, tile.z, tileSize, landTiles)
      dummy.position.set(tile.x, 0.25, tile.z)
      dummy.rotation.set(0, layout.rotation, 0)
      dummy.updateMatrix()

      if (layout.type === 'center') this.meshCenter.setMatrixAt(countCenter++, dummy.matrix)
      else if (layout.type === 'edge') this.meshEdge.setMatrixAt(countEdge++, dummy.matrix)
      else this.meshCorner.setMatrixAt(countCorner++, dummy.matrix)
    })

    this.meshCenter.count = countCenter
    this.meshEdge.count = countEdge
    this.meshCorner.count = countCorner
    this.meshCenter.instanceMatrix.needsUpdate = true
    this.meshEdge.instanceMatrix.needsUpdate = true
    this.meshCorner.instanceMatrix.needsUpdate = true

    this.elementManager.updateElements(landTiles)

    // --- ETAPE 2 : UPDATE EAU (AUTOTILING) ---
    const waterCounts: Record<WaterCategory, number> = {
      open: 0,
      '1side': 0,
      '2sides': 0,
      '3sides': 0,
      '4sides': 0,
    }

    const halfSize = (WORLD_SIZE * tileSize) / 2

    // On parcourt toute la zone du monde pour remplir les trous avec de l'eau
    for (let x = -halfSize; x < halfSize; x += tileSize) {
      for (let z = -halfSize; z < halfSize; z += tileSize) {
        // On aligne sur la grille
        const gridX = Math.round(x / tileSize) * tileSize
        const gridZ = Math.round(z / tileSize) * tileSize

        // Si c'est de la terre, pas d'eau ici
        if (landSet.has(`${gridX},${gridZ}`)) continue

        // Analyse des voisins (Nord, Sud, Est, Ouest)
        const n = landSet.has(`${gridX},${gridZ - tileSize}`) // Nord (Z-)
        const s = landSet.has(`${gridX},${gridZ + tileSize}`) // Sud (Z+)
        const e = landSet.has(`${gridX + tileSize},${gridZ}`) // Est (X+)
        const w = landSet.has(`${gridX - tileSize},${gridZ}`) // Ouest (X-)

        let neighborsCount = 0
        if (n) neighborsCount++
        if (s) neighborsCount++
        if (e) neighborsCount++
        if (w) neighborsCount++

        let category: WaterCategory = 'open'
        let rotationY = 0 // Rotation autour de l'axe vertical (qui est Z pour un Plane à plat ?)
        // Note: PlaneGeometry rotateX(-PI/2) met le plan à plat. L'axe de rotation "sur la table" devient Z.

        // Logique d'orientation des textures
        // Hypothèse : Les textures '1side', '2sides', etc. sont dessinées avec la terre en HAUT (Nord).

        if (neighborsCount === 0) {
          category = 'open'
        } else if (neighborsCount === 1) {
          category = '1side'
          if (n)
            rotationY = 0 // Terre Nord -> Pas de rotation
          else if (e)
            rotationY = -Math.PI / 2 // Terre Est -> -90°
          else if (s)
            rotationY = Math.PI // Terre Sud -> 180°
          else if (w) rotationY = Math.PI / 2 // Terre Ouest -> 90°
        } else if (neighborsCount === 2) {
          category = '2sides'
          // Cas "Coin"
          if (n && e) rotationY = 0
          else if (e && s) rotationY = -Math.PI / 2
          else if (s && w) rotationY = Math.PI
          else if (w && n) rotationY = Math.PI / 2
          // Cas "Canal" (Opposés)
          // Si tu as une texture spécifique 'canal', ajoute une catégorie. Sinon on utilise '2sides' ou 'open'
          else if (n && s) {
            category = '2sides'
            rotationY = 0
          } // Ou une texture canal
          else if (e && w) {
            category = '2sides'
            rotationY = Math.PI / 2
          }
        } else if (neighborsCount === 3) {
          category = '3sides'
          // On oriente vers le "vide" (l'ouverture)
          if (!s)
            rotationY = 0 // Vide au Sud (donc Terre N, E, O)
          else if (!w) rotationY = -Math.PI / 2
          else if (!n) rotationY = Math.PI
          else if (!e) rotationY = Math.PI / 2
        } else {
          category = '4sides'
        }

        // Ajout à l'instance
        const mesh = this.waterMeshes[category]
        if (mesh) {
          // Position Y=0 (légèrement sous la terre qui est à 0.25)
          dummy.position.set(gridX, 0, gridZ)
          // Rotation : -PI/2 sur X pour mettre à plat + RotationY calculée sur Z
          dummy.rotation.set(-Math.PI / 2, 0, rotationY)
          dummy.updateMatrix()
          mesh.setMatrixAt(waterCounts[category]++, dummy.matrix)
        }
      }
    }

    // Mise à jour finale des meshs d'eau
    ;(Object.keys(this.waterMeshes) as WaterCategory[]).forEach((key) => {
      const mesh = this.waterMeshes[key]
      if (mesh) {
        mesh.count = waterCounts[key]
        mesh.instanceMatrix.needsUpdate = true
      }
    })
  }

  // ---- HELPERS & EVENTS ---- //

  public isAdjacentToLand(x: number, z: number, existingTiles: TileData[]): boolean {
    const { tileSize } = this.config
    const neighbors = [
      { dx: 0, dz: tileSize },
      { dx: tileSize, dz: 0 },
      { dx: 0, dz: -tileSize },
      { dx: -tileSize, dz: 0 },
    ]
    return neighbors.some((offset) => {
      return existingTiles.some((tile) => tile.x === x + offset.dx && tile.z === z + offset.dz)
    })
  }

  public setSelection(x: number | null, z: number | null) {
    if (x === null || z === null) {
      this.selectionMesh.visible = false
      return
    }
    this.selectionMesh.position.set(x, 0.25, z) // Au dessus de l'eau
    this.selectionMesh.visible = true
  }

  private addEventListeners() {
    window.addEventListener('mousemove', this.onMouseMove)
    window.addEventListener('resize', this.onWindowResize)
    this.container?.addEventListener('mousedown', this.onMouseDown)
    this.container?.addEventListener('click', this.onMouseClick)
  }

  private onMouseDown(event: MouseEvent) {
    this.onDownPosition.set(event.clientX, event.clientY)
  }

  private onMouseMove(event: MouseEvent) {
    // Utilisation du plan invisible pour le Raycasting (car l'eau est instanciée)
    this.mouse.x = (event.clientX / window.innerWidth) * 2 - 1
    this.mouse.y = -(event.clientY / window.innerHeight) * 2 + 1

    this.raycaster.setFromCamera(this.mouse, this.camera)

    // On intersecte le plan invisible
    const intersects = this.raycaster.intersectObject(this.raycastPlane)

    if (intersects.length > 0) {
      const point = intersects[0].point
      const { tileSize } = this.config
      const halfTile = tileSize / 2
      const x = Math.floor((point.x + halfTile) / tileSize) * tileSize
      const z = Math.floor((point.z + halfTile) / tileSize) * tileSize

      // Limites du monde
      const limit = (WORLD_SIZE * tileSize) / 2
      if (Math.abs(x) < limit && Math.abs(z) < limit) {
        this.cursorMesh.position.set(x, 0.3, z) // Z=0.3 pour être au dessus de l'eau
        this.cursorMesh.visible = true
        this.config.onHover(x, z)
      } else {
        this.cursorMesh.visible = false
        this.config.onHover(NaN, NaN)
      }
    } else {
      this.cursorMesh.visible = false
      this.config.onHover(NaN, NaN)
    }
  }

  private onMouseClick(event: MouseEvent) {
    if (
      Math.abs(this.onDownPosition.x - event.clientX) > 5 ||
      Math.abs(this.onDownPosition.y - event.clientY) > 5
    ) {
      return
    }
    if (this.cursorMesh.visible && this.config.onClick) {
      this.config.onClick(this.cursorMesh.position.x, this.cursorMesh.position.z)
    }
  }

  private onWindowResize() {
    if (!this.container || !this.camera || !this.renderer) return
    const width = window.innerWidth
    const height = window.innerHeight
    const aspect = width / height
    const frustumSize = 40

    this.camera.left = (-frustumSize * aspect) / 2
    this.camera.right = (frustumSize * aspect) / 2
    this.camera.top = frustumSize / 2
    this.camera.bottom = -frustumSize / 2
    this.camera.updateProjectionMatrix()
    this.renderer.setSize(width, height)
  }

  // ---- ANIMATION LOOP ---- //
  private animate(time: number = 0) {
    this.animationId = requestAnimationFrame((t) => this.animate(t))

    // --- ANIMATION EAU ---
    if (time - this.lastWaterUpdate > WATER_ANIM_SPEED) {
      // 1. Frame suivante (0 -> 14 -> 0)
      this.currentWaterFrame = (this.currentWaterFrame + 1) % 15

      // 2. Mise à jour des textures pour chaque catégorie
      const categories: WaterCategory[] = ['open', '1side', '2sides', '3sides', '4sides']

      categories.forEach((cat) => {
        const textures = this.waterTextureSets[cat]
        const mesh = this.waterMeshes[cat]

        if (mesh && textures.length > 0) {
          const mat = mesh.material as THREE.MeshStandardMaterial
          // On assigne la texture correspondant à la frame actuelle
          if (textures[this.currentWaterFrame]) {
            mat.map = textures[this.currentWaterFrame]
            mat.needsUpdate = true
          }
        }
      })

      this.lastWaterUpdate = time
    }

    if (this.selectionMesh.visible) {
      const scale = 1 + Math.sin(time * 0.005) * 0.03
      this.selectionMesh.scale.set(scale, 1, scale)
      ;(this.selectionMesh.material as THREE.LineBasicMaterial).opacity =
        0.5 + Math.sin(time * 0.01) * 0.5
    }

    if (this.controls) {
      this.controls.update()
      // Contraintes de caméra
      const limit = (WORLD_SIZE * this.config.tileSize) / 2
      const target = this.controls.target
      target.x = Math.max(-limit, Math.min(limit, target.x))
      target.y = 1
      target.z = Math.max(-limit, Math.min(limit, target.z))
    }
    this.renderer.render(this.scene, this.camera)
  }

  // ---- CLEANUP ---- //
  public dispose() {
    cancelAnimationFrame(this.animationId)

    window.removeEventListener('mousemove', this.onMouseMove)
    window.removeEventListener('resize', this.onWindowResize)
    this.container?.removeEventListener('click', this.onMouseClick)
    this.container?.removeEventListener('mousedown', this.onMouseDown)

    // Nettoyage des textures
    Object.values(this.waterTextureSets).forEach((texArray) => {
      texArray.forEach((t) => t.dispose())
    })

    if (this.scene) {
      this.scene.traverse((object) => {
        if (object instanceof THREE.Mesh) {
          if (object.geometry) object.geometry.dispose()
          if (object.material) {
            if (Array.isArray(object.material)) object.material.forEach((m: any) => m.dispose())
            else object.material.dispose()
          }
        }
      })
      this.scene.clear()
    }

    if (this.renderer) {
      this.renderer.dispose()
      this.renderer.forceContextLoss()
      if (this.renderer.domElement && this.renderer.domElement.parentNode) {
        this.renderer.domElement.parentNode.removeChild(this.renderer.domElement)
      }
    }

    if (this.elementManager) this.elementManager.dispose()
    if (this.controls) this.controls.dispose()
  }
}

```

---
### File: src/components/game/logic/WorldElementsManager.ts
---

```ts
import * as THREE from 'three'
import { ITEM_REGISTRY } from '../config/ItemRegistery'
import { TileData } from './LandSceneManager'

export class WorldElementManager {
  private scene: THREE.Scene
  private meshMap: Map<string, THREE.InstancedMesh> = new Map()
  private dummy: THREE.Object3D = new THREE.Object3D()

  constructor(scene: THREE.Scene) {
    this.scene = scene
  }

  public updateElements(tiles: TileData[]) {
    // 1. Group tiles by their contentId
    const groups: Record<string, TileData[]> = {}

    tiles.forEach((tile) => {
      if (tile.contentId && ITEM_REGISTRY[tile.contentId]) {
        if (!groups[tile.contentId]) groups[tile.contentId] = []
        groups[tile.contentId].push(tile)
      }
    })

    // 2. Process each group
    for (const [itemId, config] of Object.entries(ITEM_REGISTRY)) {
      const itemsToRender = groups[itemId] || []

      // Get or Create the InstancedMesh for this item type
      let mesh = this.meshMap.get(itemId)

      if (!mesh) {
        // Create new InstancedMesh with buffer for 1000 items (resizable)
        mesh = new THREE.InstancedMesh(config.geometry, config.material, 2000)
        mesh.receiveShadow = true
        mesh.castShadow = true
        this.scene.add(mesh)
        this.meshMap.set(itemId, mesh)
      }

      // 3. Update instances
      mesh.count = itemsToRender.length

      itemsToRender.forEach((tile, index) => {
        this.dummy.position.set(tile.x, 0.25 + config.yOffset, tile.z)
        this.dummy.scale.set(config.scale, config.scale, config.scale)
        this.dummy.updateMatrix()

        mesh!.setMatrixAt(index, this.dummy.matrix)
      })

      mesh.instanceMatrix.needsUpdate = true
    }
  }

  public dispose() {
    this.meshMap.forEach((mesh) => {
      this.scene.remove(mesh)
      mesh.geometry.dispose()
      // Don't dispose shared materials here if they are consts in Registry,
      // or handle carefully.
    })
    this.meshMap.clear()
  }
}

```

---
### File: src/components/game/modal_features/InventoryInModal.vue
---

```vue
<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue';
import { remult } from 'remult';
import { useAuthStore } from '@/stores/auth';
import { FlowerStatus, FlowerRarity, ItemType } from '@/shared/types';
import { UserItem } from '@/shared/user/UserItem';
import { UserFlower } from '@/shared';
import { MarketController } from '@/server/controllers/MarketController';
import { GameController } from '@/server/controllers/GameController';
import FlowerImage from '@/components/FlowerImage.vue';

const auth = useAuthStore();
const flowerRepo = remult.repo(UserFlower);
const itemRepo = remult.repo(UserItem);

const activeTab = ref<'FLOWERS' | 'ITEMS'>('FLOWERS');
const isLoading = ref(true);
const selectedObject = ref<UserFlower | UserItem | null>(null);

const rawFlowers = ref<UserFlower[]>([]);
const rawItems = ref<UserItem[]>([]);

const searchQuery = ref('');
const currentMarketPrice = ref<number | null>(null);
const activeListingCount = ref<number>(0);

type DisplaySize = 'SMALL' | 'MEDIUM' | 'LARGE';
const displaySize = ref<DisplaySize>('SMALL');

type SortOption = 'QUALITY_DESC' | 'QUALITY_ASC' | 'RARITY_DESC' | 'NAME_ASC' | 'QUANTITY_DESC';
const flowerSort = ref<SortOption>('RARITY_DESC');
const itemSort = ref<SortOption>('QUANTITY_DESC');

const fetchInventory = async () => {
    if (!auth.user) return;

    isLoading.value = true;
    try {
        const { flowers, items } = await GameController.getUserInventory()
        rawFlowers.value = flowers
        rawItems.value = items
    } catch (e) {
        console.error(e);
    } finally {
        isLoading.value = false;
    }
};

onMounted(async () => {
    if (!auth.user) await auth.fetchSessionUser();
    fetchInventory();
});

const rarityOrder: { [key in FlowerRarity]: number } = {
    'COMMON': 0,
    'UNCOMMON': 1,
    'RARE': 2,
    'EPIC': 3,
    'LEGENDARY': 4,
};

const flowers = computed(() => {
    let list = [...rawFlowers.value];

    if (searchQuery.value.trim()) {
        const q = searchQuery.value.toLowerCase();
        list = list.filter(f => f.species?.name.toLowerCase().includes(q));
    }

    switch (flowerSort.value) {
        case 'QUALITY_DESC':
            return list.sort((a, b) => b.quality - a.quality);
        case 'QUALITY_ASC':
            return list.sort((a, b) => a.quality - b.quality);
        case 'RARITY_DESC':
            return list.sort((a, b) => {
                const rA = rarityOrder[a.species?.rarity || 'COMMON'];
                const rB = rarityOrder[b.species?.rarity || 'COMMON'];
                return rB - rA;
            });
        case 'NAME_ASC':
            return list.sort((a, b) => (a.species?.name || '').localeCompare(b.species?.name || ''));
        default:
            return list;
    }
});

const items = computed(() => {
    let list = [...rawItems.value];

    if (searchQuery.value.trim()) {
        const q = searchQuery.value.toLowerCase();
        list = list.filter(i => i.definition?.name.toLowerCase().includes(q));
    }

    switch (itemSort.value) {
        case 'QUANTITY_DESC':
            return list.sort((a, b) => b.quantity - a.quantity);
        case 'NAME_ASC':
            return list.sort((a, b) => (a.definition?.name || '').localeCompare(b.definition?.name || ''));
        default:
            return list;
    }
});

watch(selectedObject, async (newVal) => {
    currentMarketPrice.value = null;
    activeListingCount.value = 0;

    if (newVal && isFlower(newVal) && newVal.speciesId) {
        try {
            const metrics = await MarketController.getFlowerMarketMetrics(newVal.speciesId);
            currentMarketPrice.value = metrics.lowestPrice;
            activeListingCount.value = metrics.count;
        } catch (e) {
            console.error("Error fetching market data", e);
        }
    }
});

const getRarityGlowStyle = (rarity?: FlowerRarity) => {
    const colors: Record<FlowerRarity, string> = {
        'COMMON': '#94a3b8',
        'UNCOMMON': '#34d399',
        'RARE': '#60a5fa',
        'EPIC': '#c084fc',
        'LEGENDARY': '#fbbf24'
    };

    const color = colors[rarity || 'COMMON'];

    return {
        boxShadow: `inset 0 0 12px ${color}40, 0 0 20px ${color}60`,
        borderColor: `${color}80`
    };
};

const getRarityTextColorClass = (rarity?: FlowerRarity) => {
    switch (rarity) {
        case 'COMMON': return 'text-slate-400 border-slate-400/30';
        case 'UNCOMMON': return 'text-emerald-400 border-emerald-400/30';
        case 'RARE': return 'text-blue-400 border-blue-400/30';
        case 'EPIC': return 'text-purple-400 border-purple-400/30';
        case 'LEGENDARY': return 'text-amber-400 border-amber-400/30';
        default: return 'text-slate-400 border-slate-400/30';
    }
};

const getItemTypeIcon = (type?: ItemType) => {
    switch (type) {
        case 'CONSUMABLE': return '🧪';
        case 'TOOL': return '🔨';
        case 'RESOURCE': return '🪵';
        default: return '📦';
    }
};

const isFlower = (obj: any): obj is UserFlower => {
    return obj && 'species' in obj;
};

const flowerSortOptions: { value: SortOption, label: string }[] = [
    { value: 'RARITY_DESC', label: 'Rarity (High to Low)' },
    { value: 'QUALITY_DESC', label: 'Quality (High to Low)' },
    { value: 'NAME_ASC', label: 'Name (A-Z)' },
];

const itemSortOptions: { value: SortOption, label: string }[] = [
    { value: 'QUANTITY_DESC', label: 'Quantity (High to Low)' },
    { value: 'NAME_ASC', label: 'Name (A-Z)' },
];

watch(activeTab, () => {
    selectedObject.value = null;
});
</script>

<template>
    <div class="flex h-full w-full text-slate-200 overflow-hidden">

        <div class="flex-1 flex flex-col border-r border-slate-700/50 bg-slate-900/30">

            <div class="flex border-b border-slate-700/50">
                <button @click="activeTab = 'FLOWERS'"
                    class="flex-1 py-4 text-sm font-bold uppercase tracking-wider transition-colors relative"
                    :class="activeTab === 'FLOWERS' ? 'text-emerald-400 bg-slate-800/50' : 'text-slate-500 hover:text-slate-300 hover:bg-slate-800/20'">
                    🌱 Seeds Bag
                    <div v-if="activeTab === 'FLOWERS'" class="absolute bottom-0 left-0 w-full h-0.5 bg-emerald-400">
                    </div>
                </button>
                <button @click="activeTab = 'ITEMS'"
                    class="flex-1 py-4 text-sm font-bold uppercase tracking-wider transition-colors relative"
                    :class="activeTab === 'ITEMS' ? 'text-blue-400 bg-slate-800/50' : 'text-slate-500 hover:text-slate-300 hover:bg-slate-800/20'">
                    🎒 Backpack
                    <div v-if="activeTab === 'ITEMS'" class="absolute bottom-0 left-0 w-full h-0.5 bg-blue-400"></div>
                </button>
            </div>

            <div class="flex flex-col gap-3 p-3 border-b border-slate-700/50 bg-slate-900/50">

                <div class="relative w-full">
                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                    </div>
                    <input type="text" v-model="searchQuery" placeholder="Search..."
                        class="input input-sm w-full bg-slate-800 border-slate-700 text-slate-200 pl-9 focus:outline-none focus:border-slate-500 placeholder-slate-500 transition-colors" />
                </div>

                <div class="flex items-center justify-between">
                    <div class="flex items-center gap-2">
                        <label class="text-xs text-slate-400 whitespace-nowrap">Sort by:</label>
                        <select v-if="activeTab === 'FLOWERS'" v-model="flowerSort"
                            class="select select-bordered select-xs bg-slate-800 border-slate-700 text-slate-300 focus:outline-none">
                            <option v-for="option in flowerSortOptions" :key="option.value" :value="option.value">
                                {{ option.label }}
                            </option>
                        </select>

                        <select v-if="activeTab === 'ITEMS'" v-model="itemSort"
                            class="select select-bordered select-xs bg-slate-800 border-slate-700 text-slate-300 focus:outline-none">
                            <option v-for="option in itemSortOptions" :key="option.value" :value="option.value">
                                {{ option.label }}
                            </option>
                        </select>
                    </div>

                    <div v-if="activeTab === 'FLOWERS'"
                        class="flex items-center gap-1 p-1 bg-slate-800 rounded-lg border border-slate-700/50">
                        <button @click="displaySize = 'SMALL'" class="p-1.5 rounded transition-colors"
                            :class="displaySize === 'SMALL' ? 'bg-emerald-500/20 text-emerald-400' : 'text-slate-500 hover:text-slate-300'">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20"
                                fill="currentColor">
                                <path
                                    d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                            </svg>
                        </button>
                        <button @click="displaySize = 'MEDIUM'" class="p-1.5 rounded transition-colors"
                            :class="displaySize === 'MEDIUM' ? 'bg-emerald-500/20 text-emerald-400' : 'text-slate-500 hover:text-slate-300'">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20"
                                fill="currentColor">
                                <path d="M5 4a2 2 0 012-2h6a2 2 0 012 2v14l-5-2.5L5 18V4z" />
                            </svg>
                        </button>
                        <button @click="displaySize = 'LARGE'" class="p-1.5 rounded transition-colors"
                            :class="displaySize === 'LARGE' ? 'bg-emerald-500/20 text-emerald-400' : 'text-slate-500 hover:text-slate-300'">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20"
                                fill="currentColor">
                                <rect x="3" y="3" width="14" height="14" rx="2" />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>

            <div class="flex-1 overflow-y-auto p-4 custom-scrollbar">

                <div v-if="isLoading" class="flex justify-center items-center h-full">
                    <span class="loading loading-spinner loading-lg text-emerald-500"></span>
                </div>

                <div v-else-if="(activeTab === 'FLOWERS' && flowers.length === 0) || (activeTab === 'ITEMS' && items.length === 0)"
                    class="flex flex-col items-center justify-center h-full text-slate-500 opacity-60">
                    <div class="text-4xl mb-2">🤷‍♂️</div>
                    <p v-if="searchQuery">No results found.</p>
                    <p v-else>This pocket is empty.</p>
                </div>

                <div v-if="activeTab === 'FLOWERS' && !isLoading" class="grid gap-3" :class="{
                    'grid-cols-3 sm:grid-cols-4 md:grid-cols-5': displaySize === 'LARGE',
                    'grid-cols-4 sm:grid-cols-5 md:grid-cols-6': displaySize === 'MEDIUM',
                    'grid-cols-5 sm:grid-cols-6 md:grid-cols-7': displaySize === 'SMALL'
                }">
                    <div v-for="flower in flowers" :key="flower.id" @click="selectedObject = flower"
                        class="aspect-square rounded-xl border cursor-pointer transition-all hover:scale-105 hover:shadow-lg relative group bg-slate-800/40 flex items-center justify-center"
                        :style="selectedObject?.id === flower.id ? getRarityGlowStyle(flower.species?.rarity) : { borderColor: 'rgba(51, 65, 85, 0.5)' }">

                        <div class="w-full h-full p-2 flex items-center justify-center">
                            <FlowerImage :slug="flower.species?.slugName || ''" status="SEED" type="icon" size="100%"
                                class="drop-shadow-md opacity-90 group-hover:opacity-100" />
                        </div>

                        <div
                            class="absolute top-1 right-1 text-[10px] font-mono bg-black/50 px-1 rounded text-white backdrop-blur-sm">
                            Q{{ Math.round(flower.quality * 100) }}
                        </div>
                    </div>
                </div>

                <div v-if="activeTab === 'ITEMS' && !isLoading"
                    class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 gap-3">
                    <div v-for="item in items" :key="item.id" @click="selectedObject = item"
                        class="aspect-square rounded-xl border border-slate-700/50 bg-slate-800/40 cursor-pointer transition-all hover:scale-105 hover:bg-slate-700 hover:border-blue-500/50 relative group"
                        :class="{ 'ring-2 ring-blue-400 bg-slate-700': selectedObject?.id === item.id }">
                        <div class="w-full h-full p-2 flex items-center justify-center">
                            <img :src="item.definition?.assetUrl"
                                class="w-full h-full object-contain drop-shadow-md opacity-90 group-hover:opacity-100" />
                        </div>

                        <div
                            class="absolute bottom-1 right-1 bg-slate-900 text-slate-200 text-xs font-bold px-1.5 py-0.5 rounded border border-slate-700">
                            x{{ item.quantity }}
                        </div>

                        <div class="absolute top-1 left-1 opacity-50 text-xs">
                            {{ getItemTypeIcon(item.definition?.type) }}
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <div class="w-80 flex flex-col bg-slate-900/80 backdrop-blur-xl border-l border-slate-700/50 p-6 relative">
            <transition name="fade" mode="out-in">
                <div v-if="!selectedObject"
                    class="flex-1 flex flex-col items-center justify-center text-center text-slate-500">
                    <div
                        class="w-16 h-16 rounded-full bg-slate-800 mb-4 flex items-center justify-center text-2xl animate-pulse">
                        👆
                    </div>
                    <p class="text-sm">Select an item to view details</p>
                </div>

                <div v-else-if="isFlower(selectedObject)" :key="selectedObject.id" class="flex flex-col h-full">
                    <div class="flex justify-center mb-6">
                        <div class="w-32 h-32 rounded-2xl bg-slate-900/50 border shadow-lg transition-all duration-300 flex items-center justify-center relative overflow-hidden"
                            :style="getRarityGlowStyle(selectedObject.species?.rarity)">

                            <FlowerImage :slug="selectedObject.species?.slugName || ''" status="SEED" type="sprite"
                                size="96px" class="drop-shadow-[0_2px_4px_rgba(0,0,0,0.5)] scale-125" />
                        </div>
                    </div>

                    <div class="mb-4">
                        <div class="flex items-center justify-between mb-1">
                            <h2 class="text-xl font-bold text-white">{{ selectedObject.species?.name }}</h2>
                            <span class="text-xs px-2 py-0.5 rounded border uppercase font-bold"
                                :class="getRarityTextColorClass(selectedObject.species?.rarity)">
                                {{ selectedObject.species?.rarity }}
                            </span>
                        </div>
                        <p class="text-xs text-slate-500 uppercase tracking-widest font-bold mb-2">Seed</p>
                        <p class="text-sm text-slate-400 italic leading-relaxed">
                            {{ selectedObject.species?.description }}
                        </p>
                    </div>

                    <div class="bg-slate-800/40 p-3 rounded-lg border border-slate-700/50 mb-4">
                        <div class="flex justify-between items-center mb-2 pb-2 border-b border-slate-700/30">
                            <span class="text-xs font-bold text-slate-400 uppercase">Market Data</span>
                            <span class="text-xs text-slate-500">{{ activeListingCount }} Listings</span>
                        </div>
                        <div class="flex justify-between items-end">
                            <span class="text-xs text-slate-400">Est. Market Value</span>
                            <div v-if="currentMarketPrice !== null"
                                class="text-lg font-mono text-emerald-400 font-bold">
                                {{ currentMarketPrice }} <span class="text-xs font-normal">Sap</span>
                            </div>
                            <div v-else class="text-sm text-slate-500 italic">
                                Unavailable
                            </div>
                        </div>
                    </div>

                    <div class="space-y-3 mb-auto">
                        <div class="bg-slate-800/50 p-3 rounded-lg border border-slate-700/50">
                            <div class="flex justify-between text-xs mb-1">
                                <span class="text-slate-400">Quality</span>
                                <span class="text-emerald-400 font-mono">{{ Math.round(selectedObject.quality * 100)
                                    }}%</span>
                            </div>
                            <progress class="progress progress-success w-full h-1.5"
                                :value="selectedObject.quality * 100" max="100"></progress>
                        </div>

                        <div
                            class="bg-slate-800/50 p-3 rounded-lg border border-slate-700/50 flex justify-between items-center">
                            <span class="text-xs text-slate-400">Growth Time</span>
                            <span class="text-sm text-slate-200">
                                {{ Math.round((selectedObject.species?.growthDuration || 0) / 60) }} min
                            </span>
                        </div>
                    </div>

                    <div class="mt-6 space-y-2">
                        <button class="btn btn-primary w-full shadow-lg shadow-emerald-500/20">
                            Plant in Garden
                        </button>
                        <button class="btn btn-ghost btn-sm w-full text-slate-400 hover:text-red-400">
                            Trash
                        </button>
                    </div>
                </div>

                <div v-else :key="`item-${selectedObject.id}`" class="flex flex-col h-full">
                    <div class="flex justify-center mb-6">
                        <div
                            class="w-32 h-32 rounded-2xl bg-slate-800/50 border border-slate-700 flex items-center justify-center relative overflow-hidden shadow-2xl">
                            <img :src="selectedObject.definition?.assetUrl"
                                class="w-20 h-20 object-contain drop-shadow-lg" />
                        </div>
                    </div>

                    <div class="mb-6">
                        <h2 class="text-xl font-bold text-white mb-1">{{ selectedObject.definition?.name }}</h2>
                        <div class="flex gap-2 mb-3">
                            <span class="badge badge-neutral text-xs font-mono">{{ selectedObject.definition?.type
                                }}</span>
                            <span v-if="selectedObject.definition?.isTradable"
                                class="badge badge-ghost text-xs">Tradable</span>
                        </div>
                        <p class="text-sm text-slate-400 leading-relaxed">
                            {{ selectedObject.definition?.description }}
                        </p>
                    </div>

                    <div class="space-y-3 mb-auto">
                        <div
                            class="flex items-center justify-between p-3 bg-slate-800/30 rounded-lg border border-slate-700/30">
                            <span class="text-sm text-slate-400">Quantity Owned</span>
                            <span class="text-xl font-mono font-bold text-white">{{ selectedObject.quantity }}</span>
                        </div>

                        <div
                            class="flex items-center justify-between p-3 bg-slate-800/30 rounded-lg border border-slate-700/30">
                            <span class="text-sm text-slate-400">Base Value</span>
                            <span class="text-sm font-mono text-emerald-400">
                                {{ (selectedObject.definition?.basePrice || 0) * selectedObject.quantity }} Sap
                            </span>
                        </div>
                    </div>

                    <div class="mt-6 space-y-2">
                        <button v-if="selectedObject.definition?.type === 'CONSUMABLE'"
                            class="btn btn-info w-full text-white">
                            Use Item
                        </button>
                        <button v-else class="btn btn-secondary w-full">
                            Equip / Inspect
                        </button>
                    </div>
                </div>
            </transition>
        </div>
    </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease, transform 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
    transform: translateY(10px);
}
</style>
```

---
### File: src/components/game/modal_features/MarketInModal.vue
---

```vue
<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import { remult } from 'remult'
import { useModalStore } from '@/stores/modal'
import { FlowerRarity } from '@/shared/types'
import { FlowerSpecies, MarketListing, MarketStats } from '@/shared'
import { MarketController } from '@/server/controllers/MarketController'

import { Line } from 'vue-chartjs'
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler
} from 'chart.js'
import FlowerImage from '@/components/FlowerImage.vue'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler
)

const speciesList = ref<FlowerSpecies[]>([])
const listings = ref<MarketListing[]>([])
const stats = ref<MarketStats[]>([])

const selectedSpeciesId = ref<string | null>(null)
const isLoading = ref(true)
const buyingId = ref<string | null>(null)
const timeFilter = ref<'7d' | '30d' | '1y'>('7d')
const rarityFilter = ref<FlowerRarity | 'ALL'>('ALL')

const initialPrice = ref(0)

const fetchData = async () => {
    isLoading.value = true
    try {
        const { listings: l, speciesList: sL } = await MarketController.getMarketplaceData()

        speciesList.value = sL
        listings.value = l

        if (!selectedSpeciesId.value && speciesList.value.length > 0) {
            selectedSpeciesId.value = speciesList.value[0].id
        }
    } catch (error) {
        console.error(error)
    } finally {
        isLoading.value = false
    }
}

watch([selectedSpeciesId, timeFilter], async () => {
    if (!selectedSpeciesId.value) return

    const date = new Date()
    date.setHours(0, 0, 0, 0)

    if (timeFilter.value === '7d') date.setDate(date.getDate() - 7)
    if (timeFilter.value === '30d') date.setDate(date.getDate() - 30)
    if (timeFilter.value === '1y') date.setFullYear(date.getFullYear() - 1)

    const currentStats = await MarketController.getSpeciesMarketStats(
        selectedSpeciesId.value,
        { after: date }
    )
    stats.value = currentStats

    const prevStat = await MarketController.getLastSaleStat(selectedSpeciesId.value, date)
    initialPrice.value = prevStat ? prevStat.averagePrice : 0
})

onMounted(fetchData)

const marketOverview = computed(() => {
    const map = new Map<string, { count: number, minPrice: number }>()
    listings.value.forEach(l => {
        if (!l.flower) return
        const sid = l.flower.speciesId
        const current = map.get(sid) || { count: 0, minPrice: Infinity }
        map.set(sid, {
            count: current.count + 1,
            minPrice: Math.min(current.minPrice, l.price)
        })
    })
    return map
})

const filteredSpecies = computed(() => {
    let list = speciesList.value
    if (rarityFilter.value !== 'ALL') {
        list = list.filter(s => s.rarity === rarityFilter.value)
    }
    return list
})

const selectedSpecies = computed(() =>
    speciesList.value.find(s => s.id === selectedSpeciesId.value)
)

const activeListingsForSelected = computed(() =>
    listings.value
        .filter(l => l.flower?.speciesId === selectedSpeciesId.value)
        .sort((a, b) => a.price - b.price)
)

const latestStat = computed(() => stats.value.length > 0 ? stats.value[stats.value.length - 1] : null)

const chartData = computed(() => {
    const isYearly = timeFilter.value === '1y';

    const endDate = new Date()
    endDate.setHours(0, 0, 0, 0)
    const startDate = new Date(endDate)

    if (timeFilter.value === '7d') startDate.setDate(startDate.getDate() - 7)
    else if (timeFilter.value === '30d') startDate.setDate(startDate.getDate() - 30)
    else startDate.setFullYear(startDate.getFullYear() - 1)

    const statsMap = new Map<string, number>()
    stats.value.forEach(s => {
        const d = new Date(s.date)
        d.setHours(0, 0, 0, 0)
        statsMap.set(d.toISOString(), s.averagePrice)
    })

    const labels: string[] = []
    const prices: number[] = []

    let lastKnownPrice = initialPrice.value

    const stepDays = isYearly ? 7 : 1;

    for (let d = new Date(startDate); d <= endDate; d.setDate(d.getDate() + stepDays)) {

        labels.push(d.toLocaleDateString(undefined, { day: 'numeric', month: 'numeric' }))

        if (isYearly) {
            const weekEnd = new Date(d);
            weekEnd.setDate(weekEnd.getDate() + 7);

            let sum = 0;

            const weekStats = stats.value.filter(s => {
                const sDate = new Date(s.date);
                return sDate >= d && sDate < weekEnd;
            });

            if (weekStats.length > 0) {
                weekStats.forEach(ws => sum += ws.averagePrice);
                const avg = Math.round(sum / weekStats.length);
                prices.push(avg);
                lastKnownPrice = avg;
            } else {
                prices.push(lastKnownPrice);
            }

        } else {
            const iso = d.toISOString()
            if (statsMap.has(iso)) {
                const price = statsMap.get(iso)!
                prices.push(price)
                lastKnownPrice = price
            } else {
                prices.push(lastKnownPrice)
            }
        }
    }

    return {
        labels,
        datasets: [
            {
                label: 'Average Price',
                data: prices,
                borderColor: '#34d399',
                backgroundColor: (context: any) => {
                    const ctx = context.chart.ctx;
                    const gradient = ctx.createLinearGradient(0, 0, 0, 200);
                    gradient.addColorStop(0, 'rgba(52, 211, 153, 0.5)');
                    gradient.addColorStop(1, 'rgba(52, 211, 153, 0)');
                    return gradient;
                },
                borderWidth: 2,
                pointRadius: (ctx: any) => {
                    const index = ctx.dataIndex;
                    const val = ctx.dataset.data[index];
                    const prev = ctx.dataset.data[index - 1];
                    return (index === 0 || index === ctx.dataset.data.length - 1 || val !== prev) ? 3 : 0;
                },
                pointHoverRadius: 6,
                pointBackgroundColor: '#10b981',
                fill: true,
                spanGaps: true,
                tension: 0.4
            }
        ]
    }
})

const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: { display: false },
        tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'rgba(15, 23, 42, 0.9)',
            titleColor: '#e2e8f0',
            bodyColor: '#34d399',
            borderColor: 'rgba(255,255,255,0.1)',
            borderWidth: 1,
            displayColors: false,
            callbacks: {
                label: (context: any) => `${context.parsed.y} Sap`
            }
        }
    },
    scales: {
        x: {
            grid: { display: false, drawBorder: false },
            ticks: { color: '#64748b', maxTicksLimit: 8 }
        },
        y: {
            grid: { color: 'rgba(255, 255, 255, 0.05)', drawBorder: false },
            ticks: { color: '#64748b' },
            beginAtZero: true
        }
    },
    interaction: {
        mode: 'nearest',
        axis: 'x',
        intersect: false
    }
}

const handleBuy = async (listing: MarketListing) => {
    if (!confirm(`Buy this flower for ${listing.price} Sap?`)) return
    buyingId.value = listing.id
    try {
        const result = await MarketController.buyListing(listing.id)
        listings.value = listings.value.filter(l => l.id !== listing.id)
        useModalStore().open({
            title: 'Success!',
            message: result.message,
            type: 'success',
            size: 'standard'
        })
    } catch (e: any) {
        alert(e.message)
    } finally {
        buyingId.value = null
    }
}

const getRarityGlowStyle = (rarity?: FlowerRarity) => {
    const colors: Record<FlowerRarity, string> = {
        'COMMON': '#94a3b8',
        'UNCOMMON': '#34d399',
        'RARE': '#60a5fa',
        'EPIC': '#c084fc',
        'LEGENDARY': '#fbbf24'
    };

    const color = colors[rarity || 'COMMON'];

    return {
        boxShadow: `inset 0 0 12px ${color}40, 0 0 20px ${color}60`,
        borderColor: `${color}80`
    };
};

const getRarityTextColorClass = (rarity?: FlowerRarity) => {
    switch (rarity) {
        case 'COMMON': return 'text-slate-400 border-slate-400/30';
        case 'UNCOMMON': return 'text-emerald-400 border-emerald-400/30';
        case 'RARE': return 'text-blue-400 border-blue-400/30';
        case 'EPIC': return 'text-purple-400 border-purple-400/30';
        case 'LEGENDARY': return 'text-amber-400 border-amber-400/30';
        default: return 'text-slate-400 border-slate-400/30';
    }
}

const getQualityColor = (quality: number = 0) => {
    if (quality >= 0.9) return 'text-amber-400';
    if (quality >= 0.7) return 'text-purple-400';
    if (quality >= 0.5) return 'text-blue-400';
    return 'text-slate-400';
}
</script>

<template>
    <div class="flex w-full h-full text-slate-200">

        <div class="w-1/3 border-r border-slate-700/50 flex flex-col bg-slate-900/30">
            <div class="p-4 border-b border-slate-700/50">
                <select v-model="rarityFilter"
                    class="select select-sm select-bordered w-full bg-slate-800 text-slate-200">
                    <option value="ALL">All Rarities</option>
                    <option v-for="r in Object.values(FlowerRarity)" :key="r" :value="r">{{ r }}</option>
                </select>
            </div>

            <div class="overflow-y-auto flex-1 custom-scrollbar">
                <div v-for="species in filteredSpecies" :key="species.id" @click="selectedSpeciesId = species.id"
                    class="p-4 cursor-pointer hover:bg-white/5 transition-colors border-b border-slate-800/50 flex items-center gap-3 group"
                    :class="{ 'bg-slate-800': selectedSpeciesId === species.id }">

                    <div class="w-10 h-10 rounded-lg bg-slate-900 flex items-center justify-center transition-all duration-300 border border-transparent"
                        :style="selectedSpeciesId === species.id ? getRarityGlowStyle(species.rarity) : {}">
                        <FlowerImage :slug="species.slugName" status="MATURE" type="icon" size="32px"
                            class="opacity-80 group-hover:opacity-100 transition-opacity" />
                    </div>

                    <div class="flex-1 min-w-0">
                        <div class="font-bold truncate text-sm"
                            :class="selectedSpeciesId === species.id ? 'text-white' : 'text-slate-300'">
                            {{ species.name }}
                        </div>

                        <div class="text-xs opacity-60 flex justify-between mt-1">
                            <span>Stock: {{ marketOverview.get(species.id)?.count || 0 }}</span>

                            <span v-if="marketOverview.get(species.id)?.count" class="text-emerald-400">
                                {{ marketOverview.get(species.id)?.minPrice }} Sap
                            </span>
                            <span v-else class="text-slate-500 italic">
                                No stock
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="w-2/3 flex flex-col bg-slate-900/50" v-if="selectedSpecies">

            <div class="p-6 border-b border-slate-700/50 flex items-start justify-between">
                <div class="flex gap-4">
                    <div class="w-20 h-20 bg-slate-900/50 rounded-xl p-2 border shadow-lg transition-all duration-300"
                        :style="getRarityGlowStyle(selectedSpecies.rarity)">
                        <FlowerImage :slug="selectedSpecies.slugName" status="MATURE" type="sprite" size="100%"
                            class="drop-shadow-[0_2px_4px_rgba(0,0,0,0.5)]" />
                    </div>
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <h2 class="text-2xl font-bold text-white">{{ selectedSpecies.name }}</h2>
                            <span class="text-xs px-2 py-0.5 rounded border uppercase font-bold tracking-wider"
                                :class="getRarityTextColorClass(selectedSpecies.rarity)">
                                {{ selectedSpecies.rarity }}
                            </span>
                        </div>
                        <p class="text-sm text-slate-400 max-w-md">{{ selectedSpecies.description }}</p>
                    </div>
                </div>

                <div class="flex flex-col items-end gap-2">
                    <div class="text-right">
                        <div class="text-xs text-slate-400 mb-0.5 uppercase tracking-wide">Lowest Ask</div>

                        <div v-if="marketOverview.get(selectedSpecies.id)?.count"
                            class="text-3xl font-mono font-bold text-emerald-400 leading-none">
                            {{ marketOverview.get(selectedSpecies.id)?.minPrice }}
                            <span class="text-sm text-emerald-600">Sap</span>
                        </div>
                        <div v-else class="text-xl font-mono text-slate-500 font-bold">
                            --
                        </div>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-4 gap-4 px-6 py-4 border-b border-slate-700/50 bg-slate-800/20">
                <div>
                    <div class="text-xs text-slate-500 uppercase">24h Vol</div>
                    <div class="font-mono text-white text-lg">{{ latestStat?.volume || 0 }}</div>
                </div>
                <div>
                    <div class="text-xs text-slate-500 uppercase">24h Avg</div>
                    <div class="font-mono text-white text-lg">{{ latestStat?.averagePrice || '--' }} <span
                            class="text-xs text-slate-500">Sap</span></div>
                </div>
                <div>
                    <div class="text-xs text-slate-500 uppercase">24h High</div>
                    <div class="font-mono text-white text-lg">{{ latestStat?.maxPrice || '--' }} <span
                            class="text-xs text-slate-500">Sap</span></div>
                </div>
                <div>
                    <div class="text-xs text-slate-500 uppercase">24h Low</div>
                    <div class="font-mono text-emerald-400 text-lg">{{ latestStat?.minPrice || '--' }} <span
                            class="text-xs text-slate-500">Sap</span></div>
                </div>
            </div>

            <div class="p-6 min-h-[200px] border-b border-slate-700/50 flex flex-col">
                <div class="flex justify-between items-center mb-4">
                    <h3 class="font-bold text-slate-300">Average Price History</h3>
                    <div class="flex gap-2 bg-slate-800 p-1 rounded-lg">
                        <button v-for="t in ['7d', '30d', '1y']" :key="t" @click="timeFilter = t as any"
                            class="px-3 py-1 text-xs rounded transition-colors"
                            :class="timeFilter === t ? 'bg-blue-600 text-white' : 'hover:text-white text-slate-400'">
                            {{ t }}
                        </button>
                    </div>
                </div>

                <div
                    class="w-full flex-1 bg-slate-800/20 rounded-lg relative overflow-hidden border border-slate-700/30 p-2">
                    <div v-if="stats.length === 0 && initialPrice === 0"
                        class="flex h-full items-center justify-center text-slate-500 text-sm">
                        No trade history available ever.
                    </div>
                    <Line v-else :data="chartData" :options="chartOptions as any" />
                </div>
            </div>

            <div class="flex-1 overflow-hidden flex flex-col p-6">
                <h3 class="font-bold text-slate-300 mb-4 flex items-center gap-2">
                    Active Listings
                    <span class="bg-slate-700 text-white text-xs px-2 py-0.5 rounded-full">
                        {{ activeListingsForSelected.length }}
                    </span>
                </h3>

                <div class="overflow-y-auto flex-1 custom-scrollbar pr-2">
                    <table class="w-full text-left border-collapse">
                        <thead class="text-xs uppercase text-slate-500 sticky top-0 bg-slate-900/90 backdrop-blur pb-2">
                            <tr>
                                <th class="pb-3 pl-2">Seller</th>
                                <th class="pb-3">Quality</th>
                                <th class="pb-3">Listed At</th>
                                <th class="pb-3 text-right">Price</th>
                                <th class="pb-3"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="listing in activeListingsForSelected" :key="listing.id"
                                class="border-b border-slate-800/50 hover:bg-white/5 transition-colors group">
                                <td class="py-3 pl-2 text-sm text-slate-300">
                                    {{ listing.seller?.tag || 'Unknown' }}
                                </td>
                                <td class="py-3 text-sm font-bold">
                                    <span :class="getQualityColor(listing.flower?.quality)">{{
                                        Math.round((listing.flower?.quality || 0) * 100) }}</span>%
                                </td>
                                <td class="py-3 text-xs text-slate-500">
                                    {{ new Date(listing.listedAt || '').toLocaleDateString() }}
                                </td>
                                <td class="py-3 text-right font-mono text-emerald-400 font-bold">
                                    {{ listing.price }}
                                </td>
                                <td class="py-3 text-right pr-2">
                                    <button @click="handleBuy(listing)" :disabled="!!buyingId"
                                        class="btn btn-xs btn-primary opacity-0 group-hover:opacity-100 transition-opacity">
                                        <span v-if="buyingId === listing.id"
                                            class="loading loading-spinner loading-xs"></span>
                                        <span v-else>Buy</span>
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>

                    <div v-if="activeListingsForSelected.length === 0" class="flex h-[50%] items-center justify-center">
                        <span class="text-slate-500 italic">
                            No one is selling this flower currently.
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
:deep(.select:focus),
:deep(.btn:focus) {
    outline: none;
}
</style>
```

---
### File: src/components/icons/DiscordIcon.vue
---

```vue
<template>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-discord"
    viewBox="0 0 16 16">
    <path
      d="M13.545 2.907a13.2 13.2 0 0 0-3.257-1.011.05.05 0 0 0-.052.025c-.141.25-.297.577-.406.833a12.2 12.2 0 0 0-3.658 0 8 8 0 0 0-.412-.833.05.05 0 0 0-.052-.025c-1.125.194-2.22.534-3.257 1.011a.04.04 0 0 0-.021.018C.356 6.024-.213 9.047.066 12.032q.003.022.021.037a13.3 13.3 0 0 0 3.995 2.02.05.05 0 0 0 .056-.019q.463-.63.818-1.329a.05.05 0 0 0-.01-.059l-.018-.011a9 9 0 0 1-1.248-.595.05.05 0 0 1-.02-.066l.015-.019q.127-.095.248-.195a.05.05 0 0 1 .051-.007c2.619 1.196 5.454 1.196 8.041 0a.05.05 0 0 1 .053.007q.121.1.248.195a.05.05 0 0 1-.004.085 8 8 0 0 1-1.249.594.05.05 0 0 0-.03.03.05.05 0 0 0 .003.041c.24.465.515.909.817 1.329a.05.05 0 0 0 .056.019 13.2 13.2 0 0 0 4.001-2.02.05.05 0 0 0 .021-.037c.334-3.451-.559-6.449-2.366-9.106a.03.03 0 0 0-.02-.019m-8.198 7.307c-.789 0-1.438-.724-1.438-1.612s.637-1.613 1.438-1.613c.807 0 1.45.73 1.438 1.613 0 .888-.637 1.612-1.438 1.612m5.316 0c-.788 0-1.438-.724-1.438-1.612s.637-1.613 1.438-1.613c.807 0 1.451.73 1.438 1.613 0 .888-.631 1.612-1.438 1.612" />
  </svg>
</template>
```

---
### File: src/components/icons/InstagramIcon.vue
---

```vue
<template>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-instagram"
    viewBox="0 0 16 16">
    <path
      d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.9 3.9 0 0 0-1.417.923A3.9 3.9 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.9 3.9 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.9 3.9 0 0 0-.923-1.417A3.9 3.9 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599s.453.546.598.92c.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.5 2.5 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.5 2.5 0 0 1-.92-.598 2.5 2.5 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233s.008-2.388.046-3.231c.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92s.546-.453.92-.598c.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92m-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217m0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334" />
  </svg>
</template>
```

---
### File: src/components/icons/navbar/HomeIcon.vue
---

```vue
<template>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
        <path
            d="M19.006 3.705a.75.75 0 1 0-.512-1.41L6 6.838V3a.75.75 0 0 0-.75-.75h-1.5A.75.75 0 0 0 3 3v4.93l-1.006.365a.75.75 0 0 0 .512 1.41l16.5-6Z" />
        <path fill-rule="evenodd"
            d="M3.019 11.114 18 5.667v3.421l4.006 1.457a.75.75 0 1 1-.512 1.41l-.494-.18v8.475h.75a.75.75 0 0 1 0 1.5H2.25a.75.75 0 0 1 0-1.5H3v-9.129l.019-.007ZM18 20.25v-9.566l1.5.546v9.02H18Zm-9-6a.75.75 0 0 0-.75.75v4.5c0 .414.336.75.75.75h3a.75.75 0 0 0 .75-.75V15a.75.75 0 0 0-.75-.75H9Z"
            clip-rule="evenodd" />
    </svg>
</template>
```

---
### File: src/components/icons/navbar/InventoryIcon.vue
---

```vue
<template>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
        <path fill-rule="evenodd"
            d="M1.5 9.832v1.793c0 1.036.84 1.875 1.875 1.875h17.25c1.035 0 1.875-.84 1.875-1.875V9.832a3 3 0 0 0-.722-1.952l-3.285-3.832A3 3 0 0 0 16.215 3h-8.43a3 3 0 0 0-2.278 1.048L2.222 7.88A3 3 0 0 0 1.5 9.832ZM7.785 4.5a1.5 1.5 0 0 0-1.139.524L3.881 8.25h3.165a3 3 0 0 1 2.496 1.336l.164.246a1.5 1.5 0 0 0 1.248.668h2.092a1.5 1.5 0 0 0 1.248-.668l.164-.246a3 3 0 0 1 2.496-1.336h3.165l-2.765-3.226a1.5 1.5 0 0 0-1.139-.524h-8.43Z"
            clip-rule="evenodd" />
        <path
            d="M2.813 15c-.725 0-1.313.588-1.313 1.313V18a3 3 0 0 0 3 3h15a3 3 0 0 0 3-3v-1.688c0-.724-.588-1.312-1.313-1.312h-4.233a3 3 0 0 0-2.496 1.336l-.164.246a1.5 1.5 0 0 1-1.248.668h-2.092a1.5 1.5 0 0 1-1.248-.668l-.164-.246A3 3 0 0 0 7.046 15H2.812Z" />
    </svg>
</template>
```

---
### File: src/components/icons/navbar/MarketIcon.vue
---

```vue
<template>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
        <path
            d="M5.223 2.25c-.497 0-.974.198-1.325.55l-1.3 1.298A3.75 3.75 0 0 0 7.5 9.75c.627.47 1.406.75 2.25.75.844 0 1.624-.28 2.25-.75.626.47 1.406.75 2.25.75.844 0 1.623-.28 2.25-.75a3.75 3.75 0 0 0 4.902-5.652l-1.3-1.299a1.875 1.875 0 0 0-1.325-.549H5.223Z" />
        <path fill-rule="evenodd"
            d="M3 20.25v-8.755c1.42.674 3.08.673 4.5 0A5.234 5.234 0 0 0 9.75 12c.804 0 1.568-.182 2.25-.506a5.234 5.234 0 0 0 2.25.506c.804 0 1.567-.182 2.25-.506 1.42.674 3.08.675 4.5.001v8.755h.75a.75.75 0 0 1 0 1.5H2.25a.75.75 0 0 1 0-1.5H3Zm3-6a.75.75 0 0 1 .75-.75h3a.75.75 0 0 1 .75.75v3a.75.75 0 0 1-.75.75h-3a.75.75 0 0 1-.75-.75v-3Zm8.25-.75a.75.75 0 0 0-.75.75v5.25c0 .414.336.75.75.75h3a.75.75 0 0 0 .75-.75v-5.25a.75.75 0 0 0-.75-.75h-3Z"
            clip-rule="evenodd" />
    </svg>
</template>
```

---
### File: src/components/icons/navbar/SettingsIcon.vue
---

```vue
<template>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6">
        <path
            d="M18.75 12.75h1.5a.75.75 0 0 0 0-1.5h-1.5a.75.75 0 0 0 0 1.5ZM12 6a.75.75 0 0 1 .75-.75h7.5a.75.75 0 0 1 0 1.5h-7.5A.75.75 0 0 1 12 6ZM12 18a.75.75 0 0 1 .75-.75h7.5a.75.75 0 0 1 0 1.5h-7.5A.75.75 0 0 1 12 18ZM3.75 6.75h1.5a.75.75 0 1 0 0-1.5h-1.5a.75.75 0 0 0 0 1.5ZM5.25 18.75h-1.5a.75.75 0 0 1 0-1.5h1.5a.75.75 0 0 1 0 1.5ZM3 12a.75.75 0 0 1 .75-.75h7.5a.75.75 0 0 1 0 1.5h-7.5A.75.75 0 0 1 3 12ZM9 3.75a2.25 2.25 0 1 0 0 4.5 2.25 2.25 0 0 0 0-4.5ZM12.75 12a2.25 2.25 0 1 1 4.5 0 2.25 2.25 0 0 1-4.5 0ZM9 15.75a2.25 2.25 0 1 0 0 4.5 2.25 2.25 0 0 0 0-4.5Z" />
    </svg>
</template>
```

---
### File: src/main.ts
---

```ts
import { createApp } from 'vue'
import App from './App.vue'

import GoogleSignInPlugin from 'vue3-google-signin'
import { createPinia } from 'pinia'
import { router } from './routes'

import './assets/globals.css'
import './assets/main.css'

const app = createApp(App)

app.use(GoogleSignInPlugin, {
  clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID || '',
})

app.use(createPinia())
app.use(router)

app.mount('#app')

```

---
### File: src/routes/index.ts
---

```ts
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import { scrollBehavior } from './scroll'
import { ROUTES_ENUM } from './routes_enum'
import { useAuthStore } from '@/stores/auth'
import { useAuthModal } from '@/components/auth/logic/useAuthModal'

declare global {
  interface ImportMeta {
    glob: (pattern: string) => Record<string, () => Promise<unknown>>
  }
}

const viewModules = import.meta.glob('../views/**/*.vue')

const routes = [] as RouteRecordRaw[]

for (const r of Object.values(ROUTES_ENUM)) {
  routes.push({
    path: r.path,
    name: r.name,
    meta: {
      title: r.windowTitle || null,
      requiresAuth: r.requiresAuth || false,
      hideLayout: r.hideLayout || false,
    },
    component: r.viewPath
      ? viewModules[`../views/${r.viewPath}`]
      : viewModules['../views/errors/404View.vue'],
    beforeEnter: r.beforeEnter,
  })
}

export const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior,
})

router.beforeEach(async (to, _, next) => {
  const auth = useAuthStore()
  await auth.fetchSessionUser()
  if (to.meta.requiresAuth && !auth.user) {
    const authModal = useAuthModal()
    authModal.openAuthModal('login')
    next()
  } else {
    next()
  }
})

```

---
### File: src/routes/routes_enum.ts
---

```ts
import InventoryInModal from '@/components/game/modal_features/InventoryInModal.vue'
import MarketInModal from '@/components/game/modal_features/MarketInModal.vue'
import { useAuthStore } from '@/stores/auth'
import { useModalStore } from '@/stores/modal'
import { remult } from 'remult'
import type {
  NavigationGuardNext,
  RouteLocationNormalizedGeneric,
  RouteLocationNormalizedLoadedGeneric,
} from 'vue-router'

interface RouteConfig {
  name: string
  path: string
  pathDyn?: (...args: any[]) => string
  windowTitle?: string
  windowTitleDyn?: (...args: any[]) => string
  viewPath?: string
  beforeEnter?: (
    to: RouteLocationNormalizedGeneric,
    fro: RouteLocationNormalizedLoadedGeneric,
    next: NavigationGuardNext,
  ) => any
  requiresAuth?: boolean
  hideLayout?: boolean
}

export const ROUTES_ENUM = {
  HOME: {
    name: 'home',
    path: '/',
    windowTitle: 'Explore',
    viewPath: 'HomeView.vue',
  },

  WIKI: {
    name: 'wiki',
    path: '/wiki',
    windowTitle: 'Wiki',
    viewPath: 'WikiView.vue',
  },

  ABOUT: {
    name: 'about',
    path: '/about',
    windowTitle: 'About',
    viewPath: 'AboutView.vue',
  },

  CONTACT: {
    name: 'contact',
    path: '/contact',
    windowTitle: 'Contact',
    viewPath: 'ContactView.vue',
  },

  // User routes
  LOGIN: {
    name: 'login',
    path: '/login',
    windowTitle: 'Login',
    viewPath: 'user/LoginView.vue',
  },
  SIGNUP: {
    name: 'signup',
    path: '/signup',
    windowTitle: 'Sign Up',
    viewPath: 'user/SignupView.vue',
  },
  LOGOUT: {
    name: 'logout',
    path: '/logout',
    windowTitle: 'Logout',
    beforeEnter: async (_, __, next) => {
      const auth = useAuthStore()
      await auth.logout()
      next(ROUTES_ENUM.HOME.path)
    },
  },

  // GAME

  LAND: {
    name: 'land',
    path: '/land',
    windowTitle: 'My Land',
    viewPath: 'game/LandView.vue',
    hideLayout: true,
    requiresAuth: true,
  },

  USER_LAND: {
    name: 'userLand',
    path: '/land/:tag',
    pathDyn: (tag: string) => `/land/${tag}`,
    windowTitleDyn: (tag: string) => `${tag}'s Land`,
    viewPath: 'game/LandView.vue',
    hideLayout: true,
  },

  CURRENT_USER_PROFILE: {
    name: 'currentUserProfile',
    path: '/p',
    windowTitle: 'My Profile',
    viewPath: 'game/UserProfileView.vue',
  },

  USER_PROFILE: {
    name: 'userProfile',
    path: '/p/:tag',
    pathDyn: (tag: string) => `/p/${tag}`,
    windowTitleDyn: (tag: string) => `${tag}'s Profile`,
    viewPath: 'game/UserProfileView.vue',
  },

  SETTINGS: {
    name: 'userSettings',
    path: '/p/:tag/settings',
    pathDyn: (tag: string) => `/p/${tag}/settings`,
    viewPath: 'user/SettingsView.vue',
  },

  MARKET: {
    name: 'market',
    path: '/market',
    viewPath: 'game/MarketView.vue',
  },

  LAND_MARKET: {
    name: 'landMarket',
    path: '/land/market',
    beforeEnter: async (_, __, next) => {
      const modal = useModalStore()
      modal.open({
        title: 'Marketplace',
        component: MarketInModal,
        size: 'fullscreen',
        fullscreenSideBarMargin: true,
        closingPath: ROUTES_ENUM.LAND.path,
      })

      next()
    },
    viewPath: 'game/LandView.vue',
    hideLayout: true,
  },

  INVENTORY: {
    name: 'inventory',
    path: '/land/inventory',
    hideLayout: true,
    beforeEnter: async (_, __, next) => {
      const modal = useModalStore()
      modal.open({
        title: 'Inventory',
        component: InventoryInModal,
        size: 'fullscreen',
        fullscreenSideBarMargin: true,
        closingPath: ROUTES_ENUM.LAND.path,
      })

      next()
    },
    viewPath: 'game/LandView.vue',
  },

  FLORADEX: {
    name: 'floradex',
    path: '/floradex',
    windowTitle: 'FloraDex',
    viewPath: 'game/FloraDexView.vue',
  },

  SUPPORT: {
    name: 'support',
    path: '/support',
    windowTitle: 'Support',
    viewPath: 'user/SupportView.vue',
  },

  ADMIN_DB_MANAGER: {
    name: 'adminDBFuncs',
    path: '/admin/db',
    windowTitle: 'Admin DB Manager',
    viewPath: 'admin/DBManagerView.vue',
  },

  ADMIN_MANAGER: {
    name: 'adminManager',
    path: '/admin/...',
    windowTitle: 'Admin | Manager',
    viewPath: 'admin/ManagerView.vue',
    beforeEnter: (to, _, next) => {
      if (!remult.isAllowed('admin')) {
        next({
          name: 'notFound',
          params: { pathMatch: to.path.substring(1).split('/') },
          replace: true,
        })
      } else {
        next()
      }
    },
  },

  // Error routes
  NOT_FOUND: {
    name: 'notFound',
    path: '/:pathMatch(.*)*',
    windowTitle: 'Page Not Found',
    viewPath: 'errors/404View.vue',
  },
} satisfies Record<string, RouteConfig>

```

---
### File: src/routes/scroll.ts
---

```ts
import type { RouteLocationNormalized, RouterScrollBehavior } from "vue-router"

export const scrollBehavior: RouterScrollBehavior = (to: RouteLocationNormalized) => {
    if (to.hash) {
        return {
            el: to.hash,
            behavior: 'smooth'
        }
    } else {
        return { top: 0 }
    }
}
```

---
### File: src/server/_seedMarket.ts
---

```ts
// server/seedMarket.ts
import { remult } from 'remult'
import { FlowerRarity, FlowerStatus, FlowerAvailability } from '../shared/types'
import {
  FlowerSpecies,
  MarketHistory,
  MarketListing,
  MarketStats,
  User,
  UserFlower,
} from '@/shared'

// --- CONFIGURATION ---
const BOT_COUNT = 5
const HISTORY_DAYS = 30
const LISTINGS_PER_SPECIES = 4

// Fake Data Definitions
const SPECIES_DATA = [
  { name: 'Sun Petal', rarity: FlowerRarity.COMMON, basePrice: 20, color: 'gold' },
  { name: 'Dew Drop', rarity: FlowerRarity.COMMON, basePrice: 25, color: 'cyan' },
  { name: 'Ruby Rose', rarity: FlowerRarity.UNCOMMON, basePrice: 80, color: 'crimson' },
  { name: 'Night Shade', rarity: FlowerRarity.UNCOMMON, basePrice: 120, color: 'indigo' },
  { name: 'Crystal Lily', rarity: FlowerRarity.RARE, basePrice: 400, color: 'white' },
  { name: 'Void Orchid', rarity: FlowerRarity.EPIC, basePrice: 1500, color: 'purple' },
  { name: 'Golden Lotus', rarity: FlowerRarity.LEGENDARY, basePrice: 5000, color: 'orange' },
]

export async function seedMarketData() {
  console.log('🌱 Starting Market Seeding...')

  const userRepo = remult.repo(User)
  const speciesRepo = remult.repo(FlowerSpecies)
  const flowerRepo = remult.repo(UserFlower)
  const listingRepo = remult.repo(MarketListing)
  const historyRepo = remult.repo(MarketHistory)
  const statsRepo = remult.repo(MarketStats)

  // 1. Create Species (if they don't exist)
  const speciesMap = new Map<string, FlowerSpecies>()

  for (const data of SPECIES_DATA) {
    let species = await speciesRepo.findFirst({ name: data.name })
    if (!species) {
      species = await speciesRepo.insert({
        name: data.name,
        description: `A beautiful ${data.rarity.toLowerCase()} flower found in BloomScape.`,
        rarity: data.rarity,
        availability: FlowerAvailability.WILD,
        assetUrl: `https://placehold.co/64x64/${data.color}/white?text=${data.name.charAt(0)}`, // Placeholder Image
        spriteUrl: `https://placehold.co/200x200/${data.color}/white?text=Sprite`, // Placeholder Sprite
        growthDuration: 3600,
      })
    }
    speciesMap.set(data.name, species)
  }
  console.log(`✅ Verified ${speciesMap.size} Flower Species`)

  // 2. Create Bot Users
  const bots: User[] = []
  for (let i = 1; i <= BOT_COUNT; i++) {
    const tag = `TraderBot_${i}`
    let bot = await userRepo.findFirst({ tag })
    if (!bot) {
      bot = await userRepo.insert({
        tag,
        sap: 100000,
        email: `bot${i}@bloomscape.com`,
        passwordHash: 'hashed_dummy',
        description: 'I am a market simulation bot.',
      })
    }
    bots.push(bot)
  }
  console.log(`✅ Verified ${bots.length} Bot Users`)

  // 3. Generate History & Stats (The Time Machine)
  // We loop backwards from today to 30 days ago

  console.log('⏳ Generating Historical Data (this might take a moment)...')

  // Clear old stats to regenerate fresh ones
  // await Promise.all((await statsRepo.find()).map(s => statsRepo.delete(s))) // Optional: Uncomment to wipe stats first

  const today = new Date()

  for (const [name, species] of Array.from(speciesMap)) {
    const basePrice = SPECIES_DATA.find((s) => s.name === name)!.basePrice

    for (let d = HISTORY_DAYS; d >= 0; d--) {
      const date = new Date()
      date.setDate(today.getDate() - d)
      date.setHours(12, 0, 0, 0) // Midday

      // Check if stats already exist for this day (to avoid duplicates if script runs twice)
      const existingStat = await statsRepo.count({
        speciesId: species.id,
        date: {
          $gte: new Date(date.setHours(0, 0, 0, 0)),
          $lt: new Date(date.setHours(23, 59, 59, 999)),
        },
      })
      if (existingStat > 0) continue

      // Simulate Volatility: Price varies by +/- 20% + a random daily trend
      const volatility = basePrice * 0.2
      const dailyTrend = Math.sin(d) * (basePrice * 0.1) // Makes a wave pattern
      const avgPrice = Math.floor(
        basePrice + dailyTrend + (Math.random() * volatility - volatility / 2),
      )

      // Simulate 3-10 sales per day
      const salesCount = Math.floor(Math.random() * 7) + 3
      let minPrice = Infinity
      let maxPrice = -Infinity
      let totalVolume = 0

      for (let s = 0; s < salesCount; s++) {
        const salePrice = Math.floor(avgPrice + (Math.random() * 10 - 5))
        minPrice = Math.min(minPrice, salePrice)
        maxPrice = Math.max(maxPrice, salePrice)

        // Insert individual history record (optional: disable if too many rows)
        await historyRepo.insert({
          speciesId: species.id,
          price: salePrice,
          soldAt: date,
        })
        totalVolume++
      }

      // Create Daily Stats Record (Crucial for Charts)
      await statsRepo.insert({
        speciesId: species.id,
        date: date,
        averagePrice: Math.floor((minPrice + maxPrice) / 2),
        minPrice,
        maxPrice,
        volume: totalVolume,
      })
    }
  }
  console.log('✅ Historical Data Generated')

  // 4. Generate Active Listings (The Present)
  console.log('📦 generating Active Listings...')

  // Clear old listings from bots to avoid clutter
  const botIds = bots.map((b) => b.id)
  const oldListings = await listingRepo.find({ where: { sellerId: { $in: botIds } } })
  for (const l of oldListings) {
    await listingRepo.delete(l)
  }

  for (const [name, species] of Array.from(speciesMap)) {
    const baseInfo = SPECIES_DATA.find((s) => s.name === name)!

    for (let i = 0; i < LISTINGS_PER_SPECIES; i++) {
      const seller = bots[Math.floor(Math.random() * bots.length)]

      // 1. Give the bot the flower (Seed status)
      const flower = await flowerRepo.insert({
        ownerId: seller.id,
        speciesId: species.id,
        status: FlowerStatus.SEED,
        quality: Math.random(), // 0.0 to 1.0
        waterLevel: 100,
      })

      // 2. List it on the market
      // Price varies slightly
      const listingPrice = Math.floor(baseInfo.basePrice + (Math.random() * 10 - 5))

      await listingRepo.insert({
        sellerId: seller.id,
        flowerId: flower.id,
        price: listingPrice,
        listedAt: new Date(),
      })
    }
  }

  console.log('✨ Market Seed Complete! BloomScape is open for business.')
}

```

---
### File: src/server/api.ts
---

```ts
import { AuthController } from '@/server/controllers/AuthController'

import {
  Achievement,
  ClaimLink,
  FlowerSpecies,
  Friendship,
  Island,
  MarketHistory,
  MarketListing,
  MarketStats,
  SapPurchase,
  Tile,
  User,
  UserAchievement,
  UserClaim,
  UserFlower,
  UserItem,
  Item,
} from '@/shared/'

import { remultApi } from 'remult/remult-express'

import { SqlDatabase } from 'remult'
import { BetterSqlite3DataProvider } from 'remult/remult-better-sqlite3'
import Database from 'better-sqlite3'

import { UserController } from './controllers/UserController'
import { GameController } from './controllers/GameController'
import { AdminController } from './controllers/AdminController'
import { MarketController } from './controllers/MarketController'

import dotenv from 'dotenv'
import { ReportController } from './controllers/ReportController'
import { UserReport } from '@/shared/analytics/UserReport'
import { ModerationLog } from '@/shared/analytics/ModerationLog'
import { FlowerDiscovery } from '@/shared/analytics/FlowerDiscovery'
import { ChatController } from './controllers/ChatController'
import { Chat } from '@/shared/chat/Chat'
import { ChatMessage } from '@/shared/chat/ChatMessage'
import { ChatParticipant } from '@/shared/chat/ChatParticipant'

dotenv.config({
  path: './src/server/.env',
})

// DATABASE provider

const __DBProvider = new BetterSqlite3DataProvider(
  new Database(process.env.DB_PATH || './bloomscape.sqlite'),
)
const db = new SqlDatabase(__DBProvider)

export const api = remultApi({
  dataProvider: db,
  entities: [
    UserReport,
    ModerationLog,
    FlowerDiscovery,

    User,
    Achievement,
    UserAchievement,

    FlowerSpecies,
    UserFlower,
    UserItem,

    MarketListing,
    MarketHistory,
    SapPurchase,
    MarketStats,
    Item,

    Friendship,
    ClaimLink,
    UserClaim,

    Tile,
    Island,

    Chat,
    ChatMessage,
    ChatParticipant,
  ],
  controllers: [
    AuthController,
    UserController,
    GameController,
    AdminController,
    MarketController,
    ReportController,
    ChatController,
  ],
  getUser: (req) => req.session!.user,
  admin: true, // UI Interface for admins
})

```

---
### File: src/server/controllers/AdminController.ts
---

```ts
import { BackendMethod, remult } from 'remult'
import { seedMarketData } from '../_seedMarket'
import {
  Achievement,
  FlowerSpecies,
  FlowerStatus,
  Item,
  User,
  UserAchievement,
  UserFlower,
  UserItem,
} from '@/shared'
import { ModerationLog } from '@/shared/analytics/ModerationLog'

export class AdminController {
  @BackendMethod({ allowed: 'admin' })
  static async populateMarket() {
    const isDebug = process.env.DEBUG === '1'

    console.log('Debug Mode:', isDebug)

    if (isDebug) {
      await seedMarketData()
      return 'Market Populated!'
    } else {
      throw new Error('Not allowed in production')
    }
  }

  @BackendMethod({ allowed: ['admin'] })
  static async banUser(userId: string, reason: string) {
    const userRepo = remult.repo(User)
    const logRepo = remult.repo(ModerationLog)

    const user = await userRepo.findId(userId)
    if (!user) throw new Error('User not found')

    user.banned = true
    await userRepo.save(user)

    // 2. Log Action
    await logRepo.insert({
      targetUserId: userId,
      moderatorId: remult.user!.id,
      action: 'BAN',
      reason: reason,
    })

    return { success: true, message: `User ${user.tag} has been banned.` }
  }

  @BackendMethod({ allowed: 'admin' })
  static async giveItem(userId: string, itemSlug: string, quantity: number) {
    const itemRepo = remult.repo(Item)
    const userItemRepo = remult.repo(UserItem)

    const definition = await itemRepo.findFirst({ slug: itemSlug })
    if (!definition) throw new Error('Item definition not found')

    let userItem = await userItemRepo.findFirst({ userId, itemDefinitionId: definition.id })

    if (userItem) {
      userItem.quantity += quantity
      await userItemRepo.save(userItem)
    } else {
      await userItemRepo.insert({
        userId,
        itemDefinitionId: definition.id,
        quantity,
      })
    }
    return { success: true, message: `Gave ${quantity}x ${definition.name}` }
  }

  @BackendMethod({ allowed: 'admin' })
  static async giveFlower(userId: string, speciesSlug: string, quality: number) {
    const speciesRepo = remult.repo(FlowerSpecies)
    const flowerRepo = remult.repo(UserFlower)

    const species = await speciesRepo.findFirst({ slugName: speciesSlug })
    if (!species) throw new Error('Species not found')

    await flowerRepo.insert({
      ownerId: userId,
      speciesId: species.id,
      status: FlowerStatus.SEED,
      quality: quality, // 0.0 to 1.0
      waterLevel: 100,
      plantedAt: new Date(),
    })

    return { success: true, message: `Created ${species.name} Seed (Q${quality * 100})` }
  }

  @BackendMethod({ allowed: 'admin' })
  static async giveAchievement(userId: string, achievementSlug: string) {
    const achRepo = remult.repo(Achievement)
    const userAchRepo = remult.repo(UserAchievement)

    const def = await achRepo.findFirst({ slug: achievementSlug })
    if (!def) throw new Error('Achievement not found')

    const existing = await userAchRepo.findFirst({ userId, achievementId: def.id })
    if (existing) throw new Error('User already has this achievement')

    await userAchRepo.insert({
      userId,
      achievementId: def.id,
      unlockedAt: new Date(),
    })

    return { success: true, message: `Unlocked: ${def.name}` }
  }
}

```

---
### File: src/server/controllers/AuthController.ts
---

```ts
import { BackendMethod, Controller, remult, type FindOptions } from 'remult'
import express from 'express'
import { sanitizeUser, User } from '@/shared/user/User' // Assure-toi du chemin
import { Role } from '@/shared'
import slugify from 'slugify'

declare module 'remult' {
  export interface RemultContext {
    request?: express.Request
  }
}

@Controller('auth')
export class AuthController {
  // ... (login, signup, googleLogin restent identiques à ton code, je ne les répète pas pour être concis) ...
  @BackendMethod({ allowed: true })
  static async login(tagOrEmail: string, passwd: string, rememberMe: boolean = false) {
    // ... Ton code existant ...
    // Juste un rappel : assure-toi que sanitizeUser renvoie bien tout l'objet User sans le mot de passe
    // pour que le frontend ait accès aux 'sap'.
    const users = remult.repo(User)
    const user = await users.findFirst({
      $or: [{ tag: tagOrEmail }, { email: tagOrEmail }],
    })
    if (!user) throw 'Invalid tag or email'
    const bcrypt = await import('bcrypt')
    const match = await bcrypt.compare(passwd, user.passwordHash!)
    if (!match) throw 'Invalid password'

    // Mise à jour date login
    user.lastLogin = new Date()
    await users.save(user) // Save déclenchera les triggers s'il y en a

    remult.user = sanitizeUser(user)
    const req = remult.context.request!
    req.session!['user'] = remult.user

    // Gestion cookie...
    if (rememberMe) {
      req.session!.maxAge = 1000 * 60 * 60 * 24 * 30
    } else {
      req.session!.expires = undefined
    }

    return { success: true, user: req?.session!.user }
  }

  // ... (signup, googleLogin, logout ... restent identiques) ...
  @BackendMethod({ allowed: true })
  static async signup(tag: string, email: string, passwd: string, passwdConfirm: string) {
    // ... Ton code existant ...
    // Je le remets pour le contexte si besoin, mais pas de changement de logique
    const users = remult.repo(User)
    if (await users.findFirst({ tag: tag })) throw 'A user with this tag already exists.'
    if (await users.findFirst({ email: email })) throw 'A user with this email already exists.'
    if (passwd !== passwdConfirm) throw 'Passwords do not match.'
    if (passwd.length < 6) throw 'Password must be at least 6 characters.'

    const bcrypt = await import('bcrypt')
    const hashedPassword = await bcrypt.hash(passwd, 10)
    const newUser = await users.insert({ tag, email, passwordHash: hashedPassword })

    const req = remult.context!.request!
    req.session!.user = sanitizeUser(newUser)
    return { success: true, user: req?.session!.user }
  }

  @BackendMethod({ allowed: true })
  static async googleLogin(idToken: string) {
    // ... Ton code existant ...
    const { OAuth2Client } = await import('google-auth-library')
    const client = new OAuth2Client(process.env.VITE_GOOGLE_CLIENT_ID)
    const userRepo = remult.repo(User)
    const ticket = await client.verifyIdToken({
      idToken,
      audience: process.env.VITE_GOOGLE_CLIENT_ID,
    })
    const payload = ticket.getPayload()
    if (!payload || !payload.email || !payload.sub) throw new Error('Invalid Google Token')

    const email = payload.email.toLowerCase()
    const googleId = payload.sub
    const name = payload.name || email.split('@')[0]

    let user = await userRepo.findFirst({ googleId })
    if (!user) {
      user = await userRepo.findFirst({ email })
      if (user) {
        user.googleId = googleId
        await userRepo.save(user)
      } else {
        let tag = slugify(name, { lower: true, strict: true })
        let counter = 1
        while (await userRepo.findFirst({ tag })) {
          tag = `${slugify(name, { lower: true, strict: true })}${counter}`
          counter++
        }
        user = await userRepo.insert({ tag, email, googleId, roles: [Role.USER] })
      }
    }
    const req = remult.context!.request!
    req.session!.user = sanitizeUser(user)
    return { success: true, user: req.session!.user }
  }

  @BackendMethod({ allowed: true })
  static async logout() {
    // ... Ton code existant ...
    const req = remult.context!.request
    if (req?.session) req.session = null
  }

  // --- LE CHANGEMENT IMPORTANT EST ICI ---
  @BackendMethod({ allowed: true })
  static async getSessionUser() {
    if (!remult.user) return null

    const user = await remult.repo(User).findId(remult.user.id)
    return user ? sanitizeUser(user) : null
  }

  @BackendMethod({
    allowed: () => {
      const r = remult.user?.roles ?? []
      return r.includes(Role.ADMIN) ?? false
    },
  })
  static async listUsers(options: FindOptions<User>) {
    return await remult.repo(User).find(options)
  }
}

```

---
### File: src/server/controllers/ChatController.ts
---

```ts
import { BackendMethod, remult } from 'remult'
import { Chat } from '@/shared/chat/Chat'
import { ChatParticipant } from '@/shared/chat/ChatParticipant'
import { ChatMessage } from '@/shared/chat/ChatMessage'
import { User } from '@/shared/user/User'

export class ChatController {
  @BackendMethod({ allowed: true })
  static async sendMessage(payload: { chatId?: string; targetUserId?: string; content: string }) {
    if (!remult.user) throw new Error('Not authenticated')
    if (!payload.content.trim()) throw new Error('Message cannot be empty')

    const chatRepo = remult.repo(Chat)
    const partRepo = remult.repo(ChatParticipant)
    const msgRepo = remult.repo(ChatMessage)

    let chatId = payload.chatId

    if (!chatId && payload.targetUserId) {
      const myParts = await partRepo.find({ where: { userId: remult.user.id } })
      const theirParts = await partRepo.find({ where: { userId: payload.targetUserId } })

      const existingPart = myParts.find((mp) => theirParts.some((tp) => tp.chatId === mp.chatId))

      if (existingPart) {
        chatId = existingPart.chatId
      } else {
        const newChat = await chatRepo.insert({
          createdAt: new Date(),
          lastMessageAt: new Date(),
          lastMessagePreview: 'Start of conversation',
        })

        await partRepo.insert({
          chatId: newChat.id,
          userId: remult.user.id,
          joinedAt: new Date(),
          lastReadAt: new Date(),
        })

        await partRepo.insert({
          chatId: newChat.id,
          userId: payload.targetUserId,
          joinedAt: new Date(),
        })

        chatId = newChat.id
      }
    }

    if (!chatId) throw new Error('Chat not found')

    const myPart = await partRepo.findFirst({
      chatId,
      userId: remult.user.id,
    })
    if (!myPart) throw new Error('Access denied')

    const message = await msgRepo.insert({
      chatId,
      senderId: remult.user.id,
      content: payload.content.trim(),
      createdAt: new Date(),
    })

    const chat = await chatRepo.findId(chatId)
    if (chat) {
      chat.lastMessageAt = new Date()
      chat.lastMessagePreview = payload.content.substring(0, 50)
      await chatRepo.save(chat)
    }

    myPart.lastReadAt = new Date()
    await partRepo.save(myPart)

    return message
  }

  @BackendMethod({ allowed: true })
  static async markAsRead(chatId: string) {
    if (!remult.user) throw new Error('Not authenticated')
    const partRepo = remult.repo(ChatParticipant)

    const part = await partRepo.findFirst({
      chatId,
      userId: remult.user.id,
    })

    if (part) {
      part.lastReadAt = new Date()
      await partRepo.save(part)
    }
  }

  @BackendMethod({ allowed: true })
  static async searchUsers(query: string) {
    if (!remult.user) throw new Error('Not authenticated')
    if (!query || query.length < 2) return []

    return await remult.repo(User).find({
      where: {
        tag: { $contains: query },
        id: { $ne: remult.user.id },
      },
      limit: 5,
    })
  }

  @BackendMethod({ allowed: true })
  static async getChatsMetadata(chatIds: string[]) {
    if (!remult.user) throw new Error('Not authenticated')
    if (chatIds.length === 0) return []

    const myId = remult.user.id
    const partRepo = remult.repo(ChatParticipant)

    const otherParticipants = await partRepo.find({
      where: {
        chatId: { $in: chatIds },
        userId: { $ne: myId },
      },
      include: { user: true },
    })

    return otherParticipants.map((p) => ({
      chatId: p.chatId,
      otherUser: p.user,
    }))
  }
}

```

---
### File: src/server/controllers/GameController.ts
---

```ts
import {
  Achievement,
  DiscoverySource,
  FlowerAvailability,
  FlowerSpecies,
  FlowerStatus,
  Island,
  Tile,
  User,
  UserAchievement,
  UserFlower,
  UserItem,
} from '@/shared'
import { BackendMethod, remult } from 'remult'
import { PRICES } from '../ext'
import { FlowerDiscovery } from '@/shared/analytics/FlowerDiscovery'

export class GameController {
  // --- READ ACTIONS ---

  @BackendMethod({ allowed: true })
  static async getIslandDetails(ownerId: string) {
    const islandRepo = remult.repo(Island)
    const tileRepo = remult.repo(Tile)

    const island = await islandRepo.findFirst({ ownerId })

    if (!island) {
      return null
    }

    const tiles = await tileRepo.find({
      where: { islandId: island.id },
    })

    return { island, tiles }
  }

  @BackendMethod({ allowed: true })
  static async getUserBalance(tag: string) {
    const userRepo = remult.repo(User)
    const user = await userRepo.findFirst({ tag: tag })

    if (!user) throw new Error('User could not be found.')

    return user.sap
  }

  @BackendMethod({ allowed: true })
  static async getUserInventory() {
    if (!remult.user) throw new Error('Not authenticated')

    const flowerRepo = remult.repo(UserFlower)
    const itemRepo = remult.repo(UserItem)

    const flowers = await flowerRepo.find({
      where: { ownerId: remult.user.id, status: FlowerStatus.SEED },
      include: { species: true },
    })

    const items = await itemRepo.find({
      where: { userId: remult.user.id },
      include: { definition: true },
    })

    return { flowers, items }
  }

  @BackendMethod({ allowed: true })
  static async getFloradex() {
    const user = remult.user
    if (!user) throw new Error('Not authenticated')

    const speciesRepo = remult.repo(FlowerSpecies)
    const discoveryRepo = remult.repo(FlowerDiscovery)

    const allSpecies = await speciesRepo.find({
      orderBy: { rarity: 'asc', name: 'asc' },
    })

    const myDiscoveries = await discoveryRepo.find({
      where: { userId: user.id },
    })

    const floradexData = allSpecies.map((s) => {
      const discovery = myDiscoveries.find((d) => d.speciesId === s.id)

      return {
        ...s,
        discovered: !!discovery,
        discoveryDate: discovery?.discoveredAt,
        discoverySource: discovery?.source,
        initialQuality: discovery?.initialQuality,
      }
    })

    return floradexData
  }

  static getFlowerAssetUrl(
    flowerSlugName: string,
    status: FlowerStatus = FlowerStatus.MATURE,
    type: 'icon' | 'sprite' = 'icon',
  ) {
    return `/api/images/flowers/${flowerSlugName}/${status.toLowerCase()}/${type.toLowerCase()}`
  }

  // --- WRITE ACTIONS ---

  @BackendMethod({ allowed: true })
  static async startAdventure() {
    const user = remult.user
    if (!user) throw new Error('Not connected.')

    const islandRepo = remult.repo(Island)
    const tileRepo = remult.repo(Tile)

    const existing = await islandRepo.findFirst({ ownerId: user.id })
    if (existing) throw new Error('Adventure has already started !')

    const island = await islandRepo.insert({
      ownerId: user.id,
      name: `${user?.tag || 'Unknown'}'s Island`,
    })

    const initialTiles = []
    for (let x = -2; x <= 2; x += 2) {
      for (let z = -2; z <= 2; z += 2) {
        initialTiles.push({
          islandId: island.id,
          x: x,
          z: z,
          type: 'land',
        })
      }
    }

    // Insert loop
    for (const t of initialTiles) {
      await tileRepo.insert(t as any)
    }

    return island
  }

  @BackendMethod({ allowed: true })
  static async buyLand(x: number, z: number) {
    const currentUser = remult.user
    if (!currentUser) throw new Error('Not Authenticated')

    const tileRepo = remult.repo(Tile)
    const islandRepo = remult.repo(Island)

    const island = await islandRepo.findFirst({ ownerId: currentUser.id })
    if (!island) throw new Error('Island not found')

    const currentCount = await tileRepo.count({ islandId: island.id })

    if (currentCount >= currentUser.maxPlots) {
      throw new Error(
        `Limit reached! You can only own ${currentUser.maxPlots} plots. Level up to expand.`,
      )
    }

    const existing = await tileRepo.findFirst({
      islandId: island.id,
      x: x,
      z: z,
    })
    if (existing) throw new Error('This land is already owned.')

    await GameController.removeSap(PRICES.LAND_PLOT)

    return await tileRepo.insert({
      islandId: island.id,
      x: x,
      z: z,
      type: 'land',
      createdAt: new Date(),
    })
  }

  @BackendMethod({ allowed: true })
  static async getUserAchievements(targetUserId: string) {
    const achRepo = remult.repo(Achievement)
    const userAchRepo = remult.repo(UserAchievement)

    const allAchievements = await achRepo.find({
      orderBy: { rewardSap: 'asc' },
    })

    const userUnlocked = await userAchRepo.find({
      where: { userId: targetUserId },
    })

    const unlockedMap = new Map(userUnlocked.map((ua) => [ua.achievementId, ua.unlockedAt]))

    return allAchievements.map((ach) => ({
      ...ach,
      unlocked: unlockedMap.has(ach.id),
      unlockedAt: unlockedMap.get(ach.id),
    }))
  }

  // --- INTERNAL HELPERS (NOT EXPOSED TO API) ---

  static async removeSap(amount: number) {
    const user = remult.user
    if (!user) throw new Error('Not Authenticated')

    const userRepo = remult.repo(User)
    const dbUser = await userRepo.findId(user.id)
    if (!dbUser) throw new Error('User not found')

    if (dbUser.sap < amount) {
      throw new Error('Insufficient funds')
    }

    dbUser.sap -= amount
    await userRepo.save(dbUser)
    return dbUser.sap
  }

  static async registerDiscovery(
    userId: string,
    speciesId: string,
    quality: number,
    source: DiscoverySource,
  ) {
    const discRepo = remult.repo(FlowerDiscovery)

    const existing = await discRepo.findFirst({
      userId,
      speciesId,
    })

    if (!existing) {
      await discRepo.insert({
        userId,
        speciesId,
        initialQuality: quality,
        source,
        discoveredAt: new Date(),
      })
      return true
    }

    return false
  }
}

```

---
### File: src/server/controllers/MarketController.ts
---

```ts
import {
  MarketHistory,
  MarketListing,
  MarketStats,
  User,
  UserFlower,
  FlowerSpecies,
} from '@/shared'
import { BackendMethod, remult } from 'remult'
import { FlowerAvailability, FlowerRarity } from '@/shared/types'

export class MarketController {
  @BackendMethod({ allowed: true })
  static async buyListing(listingId: string) {
    const user = remult.user
    if (!user) throw new Error('Not authenticated')

    const listingRepo = remult.repo(MarketListing)
    const userRepo = remult.repo(User)
    const flowerRepo = remult.repo(UserFlower)
    const historyRepo = remult.repo(MarketHistory)

    const listing = await listingRepo.findId(listingId, { include: { flower: true } })
    const buyer = await userRepo.findId(user.id)

    if (!listing) throw new Error('This listing is no longer available.')
    if (!buyer) throw new Error('Buyer account not found.')
    if (listing.sellerId === buyer.id) throw new Error('You cannot buy your own listing.')

    if (buyer.sap < listing.price) {
      throw new Error(`Insufficient funds. You need ${listing.price} Sap.`)
    }

    // Process Transaction
    buyer.sap -= listing.price

    const seller = await userRepo.findId(listing.sellerId)
    if (seller) {
      seller.sap += listing.price
      await userRepo.save(seller)
    }
    await userRepo.save(buyer)

    // Transfer Ownership
    if (listing.flower) {
      listing.flower.ownerId = buyer.id
      // Reset any specific status if needed
      await flowerRepo.save(listing.flower)
    }

    // Record History
    await historyRepo.insert({
      speciesId: listing.flower?.speciesId || '',
      price: listing.price,
      soldAt: new Date(),
    })

    // Update Daily Stats
    if (listing.flower?.speciesId) {
      await MarketController.updateDailyStats(listing.flower.speciesId, listing.price)
    }

    await listingRepo.delete(listing)

    return { success: true, message: `Successfully purchased for ${listing.price} Sap!` }
  }

  @BackendMethod({ allowed: true })
  static async addListing(flowerId: string, price: number) {
    const user = remult.user
    if (!user) throw new Error('Not authenticated')

    const flowerRepo = remult.repo(UserFlower)
    const listingRepo = remult.repo(MarketListing)

    const flower = await flowerRepo.findId(flowerId)
    if (!flower) throw new Error('Flower not found.')
    if (flower.ownerId !== user.id) throw new Error('You do not own this flower.')

    const listing = listingRepo.create({
      flower: flower,
      sellerId: user.id,
      price: price,
      listedAt: new Date(),
    })

    await listingRepo.insert(listing)

    return { success: true, message: 'Listing added successfully.' }
  }

  @BackendMethod({ allowed: true })
  static async getFlowerMarketMetrics(speciesId: string) {
    const listingRepo = remult.repo(MarketListing)

    const listings = await listingRepo.find({
      where: { flowerId: speciesId },
    })

    if (listings.length === 0) {
      return { count: 0, lowestPrice: null }
    }

    let min = Infinity
    for (const l of listings) {
      if (l.price < min) min = l.price
    }

    return {
      count: listings.length,
      lowestPrice: min === Infinity ? null : min,
    }
  }

  @BackendMethod({ allowed: true })
  static async getMarketplaceData() {
    const speciesRepo = remult.repo(FlowerSpecies)
    const listingRepo = remult.repo(MarketListing)

    const listings = await listingRepo.find({
      include: { flower: true, seller: true },
    })

    const activeIds = Array.from(
      new Set(listings.map((l) => l.flower?.speciesId).filter((id) => !!id)),
    ) as string[]

    const speciesList = await speciesRepo.find({
      where: {
        $or: [
          { id: { $in: activeIds } },
          {
            availability: {
              $in: [FlowerAvailability.WILD, FlowerAvailability.SHOP_ONLY],
            },
          },
        ],
      },
      orderBy: { name: 'asc' },
    })

    return { listings, speciesList }
  }

  @BackendMethod({ allowed: true })
  static async getSpeciesMarketStats(speciesId: string, options: { after?: Date; before?: Date }) {
    const statsRepo = remult.repo(MarketStats)

    const afterDate = options.after ? new Date(options.after) : undefined
    const beforeDate = options.before ? new Date(options.before) : undefined

    const dateFilter: any = {}

    if (afterDate) {
      dateFilter.$gte = afterDate
    }

    if (beforeDate) {
      dateFilter.$lte = beforeDate
    }

    return await statsRepo.find({
      where: {
        speciesId: speciesId,
        date: dateFilter,
      },
      orderBy: { date: 'asc' },
    })
  }

  @BackendMethod({ allowed: true })
  static async getLastSaleStat(speciesId: string, beforeDate: Date) {
    const statsRepo = remult.repo(MarketStats)
    const dateLimit = new Date(beforeDate)

    return await statsRepo.findFirst(
      {
        speciesId,
        date: { $lt: dateLimit },
      },
      { orderBy: { date: 'desc' } }, // The latest known price of a flower
    )
  }

  /**
   * Calculates the recommended selling price for a specific flower
   * based on its Rarity, Quality, and current Market Conditions.
   */
  @BackendMethod({ allowed: true })
  static async getRecommendedPrice(speciesId: string, quality: number) {
    const statsRepo = remult.repo(MarketStats)
    const speciesRepo = remult.repo(FlowerSpecies)

    const species = await speciesRepo.findId(speciesId)
    if (!species) return 0

    const BASE_PRICES: Record<string, number> = {
      [FlowerRarity.COMMON]: 50,
      [FlowerRarity.UNCOMMON]: 150,
      [FlowerRarity.RARE]: 400,
      [FlowerRarity.EPIC]: 1000,
      [FlowerRarity.LEGENDARY]: 3000,
    }

    const VOLATILITY: Record<string, number> = {
      [FlowerRarity.COMMON]: 0.5,
      [FlowerRarity.UNCOMMON]: 1.0,
      [FlowerRarity.RARE]: 2.0,
      [FlowerRarity.EPIC]: 4.0,
      [FlowerRarity.LEGENDARY]: 8.0,
    }

    const lastStat = await statsRepo.findFirst({ speciesId }, { orderBy: { date: 'desc' } })

    let pivotPrice = lastStat?.averagePrice || BASE_PRICES[species.rarity] || 50

    const minFloor = (BASE_PRICES[species.rarity] || 50) * 0.2
    if (pivotPrice < minFloor) pivotPrice = minFloor

    const K = VOLATILITY[species.rarity] || 0.5
    const numerator = 1 + K * Math.pow(quality, 2)
    const denominator = 1 + K * Math.pow(0.5, 2)

    const multiplier = numerator / denominator

    return Math.round(pivotPrice * multiplier)
  }

  // Internal helper
  static async updateDailyStats(speciesId: string, price: number) {
    const statsRepo = remult.repo(MarketStats)
    const today = new Date()
    today.setHours(0, 0, 0, 0)

    let stat = await statsRepo.findFirst({ speciesId, date: today })

    if (!stat) {
      stat = statsRepo.create({
        speciesId,
        date: today,
        minPrice: price,
        maxPrice: price,
        averagePrice: price,
        volume: 1,
      })
    } else {
      const totalValue = stat.averagePrice * stat.volume + price
      stat.volume += 1
      stat.averagePrice = Math.round(totalValue / stat.volume)
      stat.minPrice = Math.min(stat.minPrice, price)
      stat.maxPrice = Math.max(stat.maxPrice, price)
    }

    await statsRepo.save(stat)
  }
}

```

---
### File: src/server/controllers/ReportController.ts
---

```ts
import { BackendMethod, remult } from 'remult'
import { ReportType } from '@/shared/types'
import { UserReport } from '@/shared/analytics/UserReport'

export class ReportController {
  @BackendMethod({ allowed: true }) // Autorisé à tout utilisateur connecté
  static async submitReport(data: { type: ReportType; title: string; description: string }) {
    // 1. Validation de sécurité (Backend)
    if (!remult.user) throw new Error('You must be logged in to submit a report.')

    if (!data.title || data.title.trim().length < 5) {
      throw new Error('Title is too short (min 5 characters).')
    }
    if (!data.description || data.description.trim().length < 10) {
      throw new Error('Description is too short. Please provide details.')
    }

    // 2. Anti-spam (Optionnel : vérifier le dernier rapport de cet user)
    const repo = remult.repo(UserReport)

    // Exemple simple : Empêcher de poster plus de 1 rapport toutes les 30 secondes
    const lastReport = await repo.findFirst(
      { reporterId: remult.user.id },
      { orderBy: { createdAt: 'desc' } },
    )

    if (lastReport && lastReport.createdAt) {
      const diff = new Date().getTime() - lastReport.createdAt.getTime()
      if (diff < 30 * 1000) {
        throw new Error('Please wait 30 seconds before sending another report.')
      }
    }

    // 3. Insertion en base
    const report = await repo.insert({
      reporterId: remult.user.id,
      type: data.type,
      title: data.title.trim(),
      description: data.description.trim(),
      createdAt: new Date(),
      status: 'OPEN',
    })

    return report
  }
}

```

---
### File: src/server/controllers/UserController.ts
---

```ts
import { BackendMethod, Controller, remult } from 'remult'
import express from 'express'

import { User } from '@/shared/user/User'

declare module 'remult' {
  export interface RemultContext {
    request?: express.Request
  }
}

@Controller('user')
export class UserController {
  @BackendMethod({ allowed: true })
  static async getUserByTag(tag: string) {
    if (!tag) return

    const userRepo = remult.repo(User)

    const user = await userRepo.findFirst({ tag: tag })

    if (!user) throw 'User could not be found.'

    return {
      success: true,
      user: user,
    }
  }
}

```

---
### File: src/server/ext.ts
---

```ts
export const PRICES = {
  LAND_PLOT: 1000,
}

```

---
### File: src/server/index.ts
---

```ts
import express from 'express'
import session from 'cookie-session'
import path from 'path'
import fs from 'fs'
import { remult } from 'remult'
import { api } from './api'
import { fileURLToPath } from 'url'
import { dirname } from 'path'

import dotenv from 'dotenv'
import { UserFlower, FlowerSpecies } from '@/shared'
dotenv.config({
  path: './src/server/.env',
})

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

const app = express()

app.use(
  session({
    name: 'session',
    keys: [process.env.SECRET || 'dev-key'],
  }),
)
app.use(express.json())

// Route updated to use :slugName instead of :speciesId
app.get('/api/images/flowers/:slugName/:status/:type', async (req, res) => {
  await api.withRemult(req, res, async () => {
    const { slugName, status, type } = req.params

    const validTypes = ['icon', 'sprite']
    const validStages = ['seed', 'sprout1', 'sprout2', 'growing1', 'growing2', 'mature', 'withered']

    if (!validTypes.includes(type) || !validStages.includes(status)) {
      return res
        .status(404)
        .send(
          'Invalid image type (icon, sprite) or flower status (seed, planted, mature, withered)',
        )
    }

    const secureDir = path.join(__dirname, '../private/assets/flowers')
    const fileName = `${status}.png`
    const realPath = path.join(secureDir, slugName, type, fileName)
    const unknownPath = path.join(secureDir, 'unknown.png')

    let allowed = false

    if (remult.user) {
      const speciesRepo = remult.repo(FlowerSpecies)
      const species = await speciesRepo.findFirst({ slugName })

      if (species) {
        const count = await remult.repo(UserFlower).count({
          ownerId: remult.user.id,
          speciesId: species.id,
        })
        if (count > 0) allowed = true
      }
    }

    if (allowed && fs.existsSync(realPath)) {
      return res.sendFile(realPath)
    }

    return res.sendFile(unknownPath)
  })
})

app.use(api)

app.get('/api', (_, res) => {
  res.json({ message: 'Hello from the server!' })
})

app.listen(3002, () => console.log('Server is running on port 3002'))

```

---
### File: src/shared/analytics/FlowerDiscovery.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'
import { FlowerSpecies } from '../flowers/FlowerSpecies'
import { DiscoverySource } from '../types'

@Entity('flower_discoveries', {
  allowApiCrud: false,
  defaultOrderBy: { discoveredAt: 'desc' },
})
export class FlowerDiscovery {
  @Fields.uuid()
  id!: string

  @Fields.string()
  userId!: string

  @Relations.toOne(() => User, 'userId')
  user?: User

  @Fields.string()
  speciesId!: string

  @Relations.toOne(() => FlowerSpecies, 'speciesId')
  species?: FlowerSpecies

  @Fields.createdAt()
  discoveredAt?: Date

  @Fields.string()
  source: DiscoverySource = DiscoverySource.UNKNOWN

  @Fields.number()
  initialQuality: number = 0
}

```

---
### File: src/shared/analytics/ModerationLog.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'

@Entity('moderation_logs', {
  allowApiCrud: 'admin',
})
export class ModerationLog {
  @Fields.uuid()
  id!: string

  @Fields.string()
  targetUserId!: string

  @Relations.toOne(() => User, 'targetUserId')
  targetUser?: User

  @Fields.string()
  moderatorId!: string

  @Relations.toOne(() => User, 'moderatorId')
  moderator?: User

  @Fields.string()
  action!: 'BAN' | 'WARN' | 'KICK' | 'UNBAN'

  @Fields.string()
  reason!: string

  @Fields.createdAt()
  createdAt?: Date
}

```

---
### File: src/shared/analytics/UserReport.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'
import { ReportStatus, ReportType } from '../types'

@Entity('reports', {
  allowApiCrud: 'admin',
})
export class UserReport {
  @Fields.uuid()
  id!: string

  @Fields.string()
  reporterId!: string

  @Relations.toOne(() => User, 'reporterId')
  reporter?: User

  @Fields.string()
  type: ReportType = ReportType.BUG

  @Fields.string()
  title!: string

  @Fields.string()
  description!: string

  @Fields.string()
  status: ReportStatus = ReportStatus.OPEN

  @Fields.createdAt()
  createdAt?: Date

  @Fields.date()
  resolvedAt?: Date
}

```

---
### File: src/shared/chat/Chat.ts
---

```ts
import { Entity, Fields } from 'remult'

@Entity('chats', {
  allowApiCrud: false,
  allowApiRead: true,
})
export class Chat {
  @Fields.uuid()
  id!: string

  @Fields.createdAt()
  createdAt?: Date

  @Fields.date()
  lastMessageAt?: Date

  @Fields.string()
  lastMessagePreview: string = ''
}

```

---
### File: src/shared/chat/ChatMessage.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'
import { Chat } from './Chat'

@Entity('chat_messages', {
  allowApiCrud: false,
  allowApiRead: true,
  defaultOrderBy: { createdAt: 'asc' },
})
export class ChatMessage {
  @Fields.uuid()
  id!: string

  @Fields.string()
  chatId!: string

  @Relations.toOne(() => Chat, 'chatId')
  chat?: Chat

  @Fields.string()
  senderId!: string

  @Relations.toOne(() => User, 'senderId')
  sender?: User

  @Fields.string()
  content!: string

  @Fields.createdAt()
  createdAt?: Date
}

```

---
### File: src/shared/chat/ChatParticipant.ts
---

```ts
import { Entity, Fields, Relations, remult } from 'remult'
import { User } from '../user/User'
import { Chat } from './Chat'

@Entity('chat_participants', {
  allowApiCrud: false,
  apiPrefilter: () => ({ userId: remult.user?.id }),
  allowApiRead: true,
})
export class ChatParticipant {
  @Fields.uuid()
  id!: string

  @Fields.string()
  chatId!: string

  @Relations.toOne(() => Chat, 'chatId')
  chat?: Chat

  @Fields.string()
  userId!: string

  @Relations.toOne(() => User, 'userId')
  user?: User

  @Fields.createdAt()
  joinedAt?: Date

  @Fields.date()
  lastReadAt?: Date
}

```

---
### File: src/shared/economy/Item.ts
---

```ts
import { Entity, Fields } from 'remult'
import { ItemType } from '../types'

@Entity('item_definitions', { allowApiCrud: 'admin' })
export class Item {
  @Fields.uuid()
  id!: string

  @Fields.string()
  slug!: string // ex: 'fertilizer_basic', 'fence_wood'

  @Fields.string()
  name!: string

  @Fields.string()
  description: string = ''

  @Fields.string()
  type: ItemType = ItemType.RESOURCE

  @Fields.integer()
  basePrice: number = 0

  @Fields.json()
  effects: any = {}

  @Fields.string()
  assetUrl!: string

  @Fields.boolean()
  isTradable: boolean = true

  @Fields.integer()
  maxStackSize: number = 50
}

```

---
### File: src/shared/economy/MarketHistory.ts
---

```ts
import { Entity, Fields } from 'remult'

@Entity('market_history', { allowApiCrud: 'admin' })
export class MarketHistory {
  @Fields.uuid()
  id!: string

  @Fields.string()
  speciesId!: string

  @Fields.integer()
  price!: number

  @Fields.createdAt()
  soldAt?: Date
}

```

---
### File: src/shared/economy/MarketListing.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'
import { UserFlower } from '../flowers/UserFlower'

@Entity('market_listings', { allowApiCrud: 'admin' })
export class MarketListing {
  @Fields.uuid()
  id!: string

  @Fields.string()
  sellerId!: string

  @Relations.toOne(() => User, 'sellerId')
  seller?: User

  @Fields.string()
  flowerId!: string

  @Relations.toOne(() => UserFlower, 'flowerId')
  flower?: UserFlower

  @Fields.integer()
  price: number = 0 // Price in Sap

  @Fields.createdAt()
  listedAt?: Date

  // TODO: Add backend validation to ensure flower.status === SEED
}

```

---
### File: src/shared/economy/MarketStat.ts
---

```ts
import { Entity, Fields } from 'remult'

@Entity('market_stats', {
  allowApiCrud: 'admin',
  defaultOrderBy: { date: 'desc' },
})
export class MarketStats {
  // works by the day

  @Fields.uuid()
  id!: string

  @Fields.string()
  speciesId!: string

  @Fields.dateOnly()
  date!: Date

  @Fields.number()
  averagePrice: number = 0

  @Fields.integer()
  minPrice: number = 0

  @Fields.integer()
  maxPrice: number = 0

  @Fields.integer()
  volume: number = 0 // nb of sells today
}

```

---
### File: src/shared/economy/SapPurchase.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'

@Entity('sap_purchases', { allowApiCrud: 'admin' })
export class SapPurchase {
  @Fields.uuid()
  id!: string

  @Fields.string()
  userId!: string
  @Relations.toOne(() => User, 'userId')
  user?: User

  @Fields.integer()
  amountSap!: number

  @Fields.number()
  amountFiat!: number // e.g. 9.99

  @Fields.string()
  currency: string = 'EUR'

  @Fields.string()
  providerTransactionId!: string // Stripe ID

  @Fields.createdAt()
  purchasedAt?: Date
}

```

---
### File: src/shared/flowers/FlowerSpecies.ts
---

```ts
import { Entity, Fields } from 'remult'
import { FlowerAvailability, FlowerRarity, FlowerWaterConsumption } from '../types'

@Entity('flower_species', { allowApiCrud: 'admin' })
export class FlowerSpecies {
  @Fields.uuid()
  id!: string

  @Fields.string()
  name!: string

  @Fields.string()
  slugName!: string

  @Fields.string()
  description: string = ''

  @Fields.string() // Enum
  rarity: FlowerRarity = FlowerRarity.COMMON

  @Fields.string() // Enum
  availability: FlowerAvailability = FlowerAvailability.WILD

  @Fields.json()
  attributes = {}

  @Fields.integer()
  growthDuration: number = 60 * 60 // In seconds (default 1h)

  @Fields.string() // Enum
  waterNeeds: FlowerWaterConsumption = FlowerWaterConsumption.NORMAL
}

```

---
### File: src/shared/flowers/UserFlower.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'
import { FlowerSpecies } from './FlowerSpecies'
import { FlowerStatus } from '../types'

@Entity('user_flowers', { allowApiCrud: 'admin' })
export class UserFlower {
  @Fields.uuid()
  id!: string

  @Fields.string()
  ownerId!: string

  @Relations.toOne(() => User, 'ownerId')
  owner?: User

  @Fields.string()
  speciesId!: string

  @Relations.toOne(() => FlowerSpecies, 'speciesId')
  species?: FlowerSpecies

  @Fields.string()
  status: FlowerStatus = FlowerStatus.SEED

  @Fields.number()
  quality: number = 0.5

  @Fields.date()
  plantedAt?: Date // Null if SEED

  @Fields.number()
  waterLevel: number = 100 // 0-100%

  @Fields.date()
  lastWateredAt?: Date

  // Isometric Grid Position (Null if SEED)
  @Fields.integer()
  gridX?: number

  @Fields.integer()
  gridY?: number

  // Helper to check if it's in inventory
  get isInInventory() {
    return this.status === FlowerStatus.SEED
  }
}

```

---
### File: src/shared/index.ts
---

```ts
// Types
export * from './types'

// Map
export * from './map/Tile'
export * from './map/Island'

// User
export * from './user/User'
export * from './user/Achievement'
export * from './user/UserAchievement'

// Flowers
export * from './flowers/FlowerSpecies'
export * from './flowers/UserFlower'
export * from './user/UserItem'

// Economy
export * from './economy/MarketListing'
export * from './economy/MarketHistory'
export * from './economy/SapPurchase'
export * from './economy/MarketStat'
export * from './economy/Item'

// Social
export * from './social/Friendship'
export * from './social/ClaimLink'
export * from './social/UserClaim'

```

---
### File: src/shared/map/Island.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'
import { Tile } from './Tile'

@Entity('islands', {
  allowApiCrud: 'admin',
})
export class Island {
  @Fields.uuid()
  id!: string

  @Fields.string()
  name: string = 'New Island'

  // Relation Back-Reference
  @Relations.toMany(() => Tile, { field: 'islandId' })
  tiles?: Tile[]

  @Fields.createdAt()
  createdAt?: Date

  @Fields.string()
  ownerId!: string

  @Relations.toOne(() => User, { field: 'ownerId' })
  owner?: User
}

```

---
### File: src/shared/map/Tile.ts
---

```ts
import { Entity, Field, Fields, Relations } from 'remult'
import { Island } from './Island'
import { TileType } from '../types'
import { FlowerSpecies } from '../flowers/FlowerSpecies'

@Entity('tiles', {
  allowApiCrud: 'admin', // TODO: Restrict logic later
})
export class Tile {
  @Fields.uuid()
  id!: string

  @Fields.integer()
  x!: number

  @Fields.integer()
  z!: number

  @Fields.string()
  type: TileType = 'land'

  @Fields.createdAt()
  createdAt?: Date

  // Relation : Une tuile appartient à une île
  @Fields.string()
  islandId!: string

  @Relations.toOne(() => Island, { field: 'islandId' })
  island?: Island

  @Fields.string()
  flowerId?: string

  @Relations.toOne(() => FlowerSpecies, { field: 'flowerId' })
  flower?: FlowerSpecies
}

```

---
### File: src/shared/social/ClaimLink.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { FlowerSpecies } from '../flowers/FlowerSpecies'

@Entity('claim_links', { allowApiCrud: 'admin' })
export class ClaimLink {
  @Fields.uuid()
  id!: string

  @Fields.string()
  code!: string

  @Fields.string()
  rewardSpeciesId!: string

  @Relations.toOne(() => FlowerSpecies, 'rewardSpeciesId')
  rewardSpecies: FlowerSpecies

  @Fields.integer()
  maxUses: number = 1

  @Fields.integer()
  currentUses: number = 0

  @Fields.date()
  expirationDate?: Date
}

```

---
### File: src/shared/social/Friendship.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'
import { FriendshipStatus } from '../types'

@Entity('friendships', { allowApiCrud: 'admin' })
export class Friendship {
  @Fields.uuid()
  id!: string

  @Fields.string()
  requesterId!: string

  @Relations.toOne(() => User, 'requesterId')
  requester?: User

  @Fields.string()
  receiverId!: string

  @Relations.toOne(() => User, 'receiverId')
  receiver?: User

  @Fields.string()
  status: FriendshipStatus = FriendshipStatus.PENDING

  @Fields.createdAt()
  since?: Date
}

```

---
### File: src/shared/social/UserClaim.ts
---

```ts
import { Entity, Fields } from 'remult'

@Entity('user_claims', { allowApiCrud: 'admin' })
export class UserClaim {
  @Fields.uuid()
  id!: string

  @Fields.string()
  userId!: string

  @Fields.string()
  claimLinkId!: string

  @Fields.createdAt()
  claimedAt?: Date
}

```

---
### File: src/shared/types.ts
---

```ts
export const Role = {
  USER: 'user',
  ADMIN: 'admin',
} as const

export type Role = (typeof Role)[keyof typeof Role]

export const FlowerRarity = {
  COMMON: 'COMMON',
  UNCOMMON: 'UNCOMMON',
  RARE: 'RARE',
  EPIC: 'EPIC',
  LEGENDARY: 'LEGENDARY',
} as const

export type FlowerRarity = (typeof FlowerRarity)[keyof typeof FlowerRarity]

export const FlowerAvailability = {
  WILD: 'WILD', // Can be found randomly
  BREEDING_ONLY: 'BREEDING_ONLY', // Result of fusion
  EVENT_ONLY: 'EVENT_ONLY', // Hidden/Link only
  SHOP_ONLY: 'SHOP_ONLY', // Bought with Sap
} as const

export type FlowerAvailability = (typeof FlowerAvailability)[keyof typeof FlowerAvailability]

export const FlowerStatus = {
  SEED: 'SEED',
  SPROUT1: 'SPROUT1',
  SPROUT2: 'SPROUT2',
  GROWING1: 'GROWING1',
  GROWING2: 'GROWING2',
  MATURE: 'MATURE',
  WITHERED: 'WITHERED',
} as const

export type FlowerStatus = (typeof FlowerStatus)[keyof typeof FlowerStatus]

export const FlowerWaterConsumption = {
  VERY_LOW: 'VERY_LOW',
  LOW: 'LOW',
  NORMAL: 'NORMAL',
  HIGH: 'HIGH',
  VERY_HIGH: 'VERY_HIGH',
} as const

export type FlowerWaterConsumption =
  (typeof FlowerWaterConsumption)[keyof typeof FlowerWaterConsumption]

export const FriendshipStatus = {
  PENDING: 'PENDING',
  ACCEPTED: 'ACCEPTED',
  BLOCKED: 'BLOCKED',
} as const

export type FriendshipStatus = (typeof FriendshipStatus)[keyof typeof FriendshipStatus]

export const TileType = {
  LAND: 'land',
  WATER: 'water',
  FOREST: 'forest',
} as const

export type TileType = (typeof TileType)[keyof typeof TileType]

export const ItemType = {
  CONSUMABLE: 'CONSUMABLE', // Fertilizer, potions
  RESOURCE: 'RESOURCE', // Wood, stone (for tool crafting)
  TOOL: 'TOOL', // Improved watering can, shovel, rake
} as const

export type ItemType = (typeof ItemType)[keyof typeof ItemType]

export const ReportType = {
  BUG: 'BUG',
  FEATURE: 'FEATURE',
  PLAYER_REPORT: 'PLAYER_REPORT',
  OTHER: 'OTHER',
} as const
export type ReportType = (typeof ReportType)[keyof typeof ReportType]

export const ReportStatus = {
  OPEN: 'OPEN',
  IN_PROGRESS: 'IN_PROGRESS',
  RESOLVED: 'RESOLVED',
  REJECTED: 'REJECTED',
} as const
export type ReportStatus = (typeof ReportStatus)[keyof typeof ReportStatus]

export const DiscoverySource = {
  WILD: 'WILD',
  BREEDING: 'BREEDING',
  MARKET: 'MARKET',
  GIFT: 'GIFT',
  UNKNOWN: 'UNKNOWN',
} as const

export type DiscoverySource = (typeof DiscoverySource)[keyof typeof DiscoverySource]

```

---
### File: src/shared/user/Achievement.ts
---

```ts
import { Entity, Fields } from 'remult'

@Entity('achievements', { allowApiCrud: 'admin' }) // Admin managed only
export class Achievement {
  @Fields.uuid()
  id!: string

  @Fields.string()
  slug!: string // e.g. "first_planting"

  @Fields.string()
  name!: string

  @Fields.string()
  description!: string

  @Fields.integer()
  rewardSap: number = 0
}

```

---
### File: src/shared/user/User.ts
---

```ts
import { Entity, Fields } from 'remult'
import { Role } from '../types'

export const sanitizeUser = (user: User) => {
  const { passwordHash, email, ...sanitized } = user
  return sanitized
}

@Entity('users', {
  allowApiCrud: 'admin', // TODO : restrict this later to
})
export class User {
  @Fields.uuid()
  id!: string

  @Fields.string()
  tag!: string

  @Fields.string({ includeInApi: false })
  email!: string

  @Fields.string()
  description: string = ''

  @Fields.string({ includeInApi: false })
  passwordHash!: string

  @Fields.number()
  sap: number = 0

  @Fields.integer()
  level: number = 1

  @Fields.integer()
  xp: number = 0

  @Fields.integer()
  score: number = 0

  @Fields.integer()
  maxPlots: number = 9

  @Fields.boolean()
  enableAds: boolean = false

  @Fields.date()
  lastAdRevenue?: Date

  @Fields.date()
  lastLogin?: Date

  @Fields.string()
  googleId: string = ''

  @Fields.createdAt()
  createdAt?: Date

  @Fields.json()
  roles: Role[] = [Role.USER]

  @Fields.boolean()
  banned: boolean = false
}

```

---
### File: src/shared/user/UserAchievement.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from './User'
import { Achievement } from './Achievement'

@Entity('user_achievements', { allowApiCrud: 'admin' })
export class UserAchievement {
  @Fields.uuid()
  id!: string

  @Fields.string()
  userId!: string

  @Relations.toOne(() => User, 'userId')
  user?: User

  @Fields.string()
  achievementId!: string

  @Relations.toOne(() => Achievement, 'achievementId')
  achievement?: Achievement

  @Fields.createdAt()
  unlockedAt?: Date
}

```

---
### File: src/shared/user/UserItem.ts
---

```ts
import { Entity, Fields, Relations } from 'remult'
import { User } from '../user/User'
import { Item } from '../economy/Item'

@Entity('user_items', { allowApiCrud: 'admin' })
export class UserItem {
  @Fields.uuid()
  id!: string

  @Fields.string()
  userId!: string

  @Relations.toOne(() => User, 'userId')
  owner?: User

  @Fields.string()
  itemDefinitionId!: string

  @Relations.toOne(() => Item, 'itemDefinitionId')
  definition?: Item

  @Fields.integer()
  quantity: number = 0
}

```

---
### File: src/stores/auth.ts
---

```ts
import { AuthController } from '@/server/controllers/AuthController'
import { defineStore } from 'pinia'
import { User } from '@/shared/user/User' // On importe l'entité complète, pas juste UserInfo
import { router } from '@/routes' // Importe ton instance de routeur exportée (pas le hook)
import { remult } from 'remult'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    // On type avec User pour avoir accès à .sap, .level, etc.
    user: null as null | User,
    returnURL: null as string | null,
  }),
  actions: {
    async login(tagOrEmail: string, password: string, rememberMe: boolean) {
      const res = await AuthController.login(tagOrEmail.toLowerCase(), password, rememberMe)

      // On caste le résultat car le Controller renvoie l'objet complet
      this.user = res.user as User

      if (this.returnURL) {
        // On utilise l'instance importée directement
        router.push(this.returnURL)
        this.returnURL = null
      }
    },

    async logout() {
      await AuthController.logout()
      this.user = null
      router.push('/login')
    },

    async signUp(tag: string, email: string, password: string, passwordConfirm: string) {
      const res = await AuthController.signup(
        tag.toLowerCase(),
        email.toLowerCase(),
        password,
        passwordConfirm,
      )
      this.user = res.user as User
    },

    async googleLogin(googleId: string) {
      const res = await AuthController.googleLogin(googleId)
      this.user = res.user as User
    },

    // Cette fonction sert maintenant de "Refresh" universel
    async fetchSessionUser() {
      // Appelle le AuthController modifié qui va chercher les données fraîches en DB
      const freshUser = await AuthController.getSessionUser()
      remult.user = freshUser as User
      this.user = freshUser as User
    },
  },
})

```

---
### File: src/stores/breakpoints.ts
---

```ts
import { defineStore } from 'pinia'

export const useBreakpoints = defineStore('breakpoints', {
  state: () => ({
    phone: '' as string,
    sm: '' as string,
    md: '' as string,
    lg: '' as string,
    xl: '' as string,
  }),
  actions: {
    getBreakpoints() {
      const styles = getComputedStyle(document.documentElement)
      this.phone = styles.getPropertyValue('--breakpoint-phone').trim()
      this.sm = styles.getPropertyValue('--breakpoint-sm').trim()
      this.md = styles.getPropertyValue('--breakpoint-md').trim()
      this.lg = styles.getPropertyValue('--breakpoint-lg').trim()
      this.xl = styles.getPropertyValue('--breakpoint-xl').trim()
    },
  },
})

```

---
### File: src/stores/chat.ts
---

```ts
import { defineStore } from 'pinia'
import { ref, computed, onUnmounted } from 'vue'
import { remult } from 'remult'
import { Chat } from '@/shared/chat/Chat'
import { ChatParticipant } from '@/shared/chat/ChatParticipant'
import { ChatMessage } from '@/shared/chat/ChatMessage'
import { User } from '@/shared/user/User'
import { ChatController } from '@/server/controllers/ChatController'
import { useAuthStore } from './auth'

export interface ChatUI extends Chat {
  otherUser?: User
  hasUnread: boolean
}

export const useChatStore = defineStore('chat', () => {
  const auth = useAuthStore()

  const isOpen = ref(false)
  const activeChatId = ref<string | null>(null)
  const searchQuery = ref('')

  const myChats = ref<ChatUI[]>([])
  const currentMessages = ref<ChatMessage[]>([])
  const globalSearchResults = ref<User[]>([])

  let unsubscribeChats: (() => void) | null = null
  let unsubscribeMessages: (() => void) | null = null

  const activeChat = computed(() => {
    return myChats.value.find((c) => c.id === activeChatId.value)
  })

  const filteredChats = computed(() => {
    if (!Array.isArray(myChats.value)) return []
    if (!searchQuery.value) return myChats.value

    const q = searchQuery.value.toLowerCase()

    return myChats.value.filter((c) => {
      const tagName = c.otherUser?.tag
      return tagName && tagName.toLowerCase().includes(q)
    })
  })

  function init() {
    if (!auth.user) return

    if (unsubscribeChats) unsubscribeChats()

    unsubscribeChats = remult
      .repo(ChatParticipant)
      .liveQuery({
        where: { userId: auth.user.id },
        include: { chat: true },
      })
      .subscribe(async (info) => {
        const participants = info.applyChanges([])
        const chatIds = participants.map((p) => p.chatId)

        if (chatIds.length === 0) {
          myChats.value = []
          return
        }

        const metadata = await ChatController.getChatsMetadata(chatIds)

        const enriched: ChatUI[] = participants.map((p) => {
          const meta = metadata.find((m) => m.chatId === p.chatId)

          const hasUnread =
            p.chat?.lastMessageAt && p.lastReadAt
              ? new Date(p.chat.lastMessageAt) > new Date(p.lastReadAt)
              : !!p.chat?.lastMessageAt

          return {
            ...p.chat!,
            otherUser: meta?.otherUser,
            hasUnread,
          }
        })

        myChats.value = enriched.sort((a, b) => {
          const da = a.lastMessageAt ? new Date(a.lastMessageAt).getTime() : 0
          const db = b.lastMessageAt ? new Date(b.lastMessageAt).getTime() : 0
          return db - da
        })
      })
  }

  function openChat(chatId: string) {
    activeChatId.value = chatId
    if (unsubscribeMessages) unsubscribeMessages()

    ChatController.markAsRead(chatId)

    unsubscribeMessages = remult
      .repo(ChatMessage)
      .liveQuery({
        where: { chatId },
        orderBy: { createdAt: 'asc' },
        include: { sender: true },
        limit: 50,
      })
      .subscribe((info) => {
        currentMessages.value = info.applyChanges(currentMessages.value)
      })
  }

  async function startChatWithUser(targetUserId: string) {
    try {
      const message = await ChatController.sendMessage({
        targetUserId,
        content: '👋',
      })
      openChat(message.chatId)
      searchQuery.value = ''
      globalSearchResults.value = []
    } catch (e) {
      console.error(e)
    }
  }

  function closeConversation() {
    activeChatId.value = null
    if (unsubscribeMessages) {
      unsubscribeMessages()
      unsubscribeMessages = null
    }
    currentMessages.value = []
  }

  async function sendMessage(text: string) {
    if (!activeChatId.value || !text.trim()) return
    try {
      await ChatController.sendMessage({
        chatId: activeChatId.value,
        content: text,
      })
    } catch (e) {
      console.error('Failed to send', e)
    }
  }

  async function performSearch() {
    try {
      globalSearchResults.value = await ChatController.searchUsers(searchQuery.value)
    } catch (e) {
      console.error(e)
      globalSearchResults.value = []
    }
  }

  function toggle() {
    isOpen.value = !isOpen.value
    if (isOpen.value && myChats.value.length === 0) {
      init()
    }
  }

  onUnmounted(() => {
    if (unsubscribeChats) unsubscribeChats()
    if (unsubscribeMessages) unsubscribeMessages()
  })

  return {
    isOpen,
    toggle,
    searchQuery,
    performSearch,
    myChats,
    filteredChats,
    globalSearchResults,
    activeChatId,
    activeChat,
    currentMessages,
    openChat,
    startChatWithUser,
    closeConversation,
    sendMessage,
    init,
  }
})

```

---
### File: src/stores/game.ts
---

```ts
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import { remult } from 'remult'
import { GameController } from '@/server/controllers/GameController'
import { Island, Tile } from '@/shared'
import { useModalStore } from './modal'

// UI Helper Type
export interface TileInteraction {
  x: number
  z: number
  id?: string
  isOwned: boolean
  isAdjacentToLand: boolean
}

export const useGameStore = defineStore('game', () => {
  const currentIsland = ref<Island | null>(null)
  const tiles = ref<Tile[]>([])

  const hoveredTile = ref<TileInteraction | null>(null)
  const selectedTile = ref<TileInteraction | null>(null)

  const isLoading = ref(false)
  const playerBalance = ref(0)

  const selectedEntity = computed(() => {
    if (!selectedTile.value) return null
    return (
      tiles.value.find((t) => t.x === selectedTile.value?.x && t.z === selectedTile.value?.z) ||
      null
    )
  })

  // --- ACTIONS ---

  async function fetchIslandData(userId: string) {
    isLoading.value = true
    currentIsland.value = null
    tiles.value = []

    try {
      const result = await GameController.getIslandDetails(userId)

      if (result) {
        currentIsland.value = result.island
        tiles.value = result.tiles
      }
    } catch (e) {
      console.error(e)
    } finally {
      isLoading.value = false
    }
  }

  async function startAdventure() {
    isLoading.value = true
    try {
      await GameController.startAdventure()
      if (remult.user) {
        await fetchIslandData(remult.user.id)
        await fetchBalance()
      }
    } catch (e: any) {
      alert(e.message)
    } finally {
      isLoading.value = false
    }
  }

  async function fetchBalance() {
    if (!remult.user) return
    try {
      playerBalance.value = await GameController.getUserBalance(remult.user.tag)
    } catch (error) {
      console.error('Error fetching balance:', error)
    }
  }

  async function buyTile(x: number, z: number) {
    if (!currentIsland.value) return

    isLoading.value = true

    try {
      const newTile = await GameController.buyLand(x, z)
      tiles.value.push(newTile)

      if (selectedTile.value && selectedTile.value.x === x && selectedTile.value.z === z) {
        selectedTile.value.isOwned = true
        selectedTile.value.id = newTile.id
      }

      await fetchBalance()
    } catch (e: any) {
      const modal = useModalStore()
      modal.open({
        title: 'Purchase Failed',
        message: e.message,
        type: 'error',
      })
    } finally {
      isLoading.value = false
    }
  }

  function getTileAt(x: number, z: number) {
    return tiles.value.find((t) => t.x === x && t.z === z)
  }

  function setHoveredTile(t: TileInteraction | null) {
    hoveredTile.value = t
  }

  function selectTile(t: TileInteraction | null) {
    selectedTile.value = t
  }

  return {
    currentIsland,
    tiles,
    hoveredTile,
    selectedTile,
    selectedEntity,
    playerBalance,
    isLoading,
    fetchIslandData,
    fetchBalance,
    startAdventure,
    buyTile,
    getTileAt,
    setHoveredTile,
    selectTile,
  }
})

```

---
### File: src/stores/modal.ts
---

```ts
import { router } from '@/routes'
import { defineStore } from 'pinia'
import { ref, markRaw, type Component } from 'vue'

export type ModalType = 'info' | 'success' | 'warning' | 'error'
export type ModalSize = 'standard' | 'large' | 'fullscreen'

export interface ModalAction {
  label: string
  onClick: () => void
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost'
}

export const useModalStore = defineStore('modal', () => {
  const isOpen = ref(false)
  const type = ref<ModalType>('info')
  const title = ref('')
  const message = ref('')
  const size = ref<ModalSize>('standard')
  const component = ref<Component | null>(null)
  const componentProps = ref<Record<string, any>>({})
  const actions = ref<ModalAction[]>([])
  const fullscreenSideBarMargin = ref(false)

  const previousPath = ref<string | null>(null)
  const closingPath = ref<string | null>(null)

  function open(payload: {
    title: string
    message?: string
    type?: ModalType
    size?: ModalSize
    component?: Component
    componentProps?: Record<string, any>
    actions?: ModalAction[]
    path?: string // false url shown when the modal is opened
    closingPath?: string // url the modal should return to when closed
    fullscreenSideBarMargin?: boolean
  }) {
    title.value = payload.title
    message.value = payload.message || ''
    type.value = payload.type || 'info'
    size.value = payload.size || 'standard'
    fullscreenSideBarMargin.value = payload.fullscreenSideBarMargin || false
    closingPath.value = payload.closingPath || null

    // Gestion du composant
    if (payload.component) {
      component.value = markRaw(payload.component)
      componentProps.value = payload.componentProps || {}
    } else {
      component.value = null
      componentProps.value = {}
    }

    // Gestion des actions
    if (payload.actions && payload.actions.length > 0) {
      actions.value = payload.actions
    } else {
      actions.value = [
        {
          label: 'Fermer',
          onClick: () => close(),
          variant: 'primary',
        },
      ]
    }

    // --- GESTION DE L'URL (ENDPOINT) ---
    if (payload.path) {
      previousPath.value = window.location.pathname
      window.history.pushState({ modalOpen: true }, '', payload.path)
    } else {
      previousPath.value = null
    }

    isOpen.value = true
  }

  function close() {
    isOpen.value = false

    // --- RESTAURATION DE L'URL ---
    if (previousPath.value) {
      window.history.pushState({}, '', previousPath.value)
      previousPath.value = null
    } else if (closingPath.value) {
      router.push(closingPath.value)
    }

    setTimeout(() => {
      title.value = ''
      message.value = ''
      size.value = 'standard'
      component.value = null
      componentProps.value = {}
      actions.value = []
    }, 300)
  }

  return {
    isOpen,
    type,
    title,
    message,
    size,
    component,
    componentProps,
    fullscreenSideBarMargin,
    actions,
    open,
    close,
  }
})

```

---
### File: src/stores/theme.ts
---

```ts
import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    theme: localStorage.getItem('theme') || 'light',
  }),
  actions: {
    setTheme(val: 'light' | 'dark') {
      this.theme = val
      document.documentElement.setAttribute('data-theme', val)
      localStorage.setItem('theme', val)
    },
    toggle() {
      this.setTheme(this.theme === 'light' ? 'dark' : 'light')
    },
    applyTheme() {
      document.documentElement.setAttribute('data-theme', this.theme)
    },
  },
})

```

---
### File: src/stores/ui.ts
---

```ts
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
  const isSidebarOpen = ref(false)
  const isSidebarHovered = ref(false)

  function toggleSidebar() {
    isSidebarOpen.value = !isSidebarOpen.value
  }

  function closeSidebar() {
    isSidebarOpen.value = false
  }

  return {
    isSidebarOpen,
    isSidebarHovered,
    toggleSidebar,
    closeSidebar,
  }
})

```

---
### File: src/views/AboutView.vue
---

```vue
<script setup lang="ts">

</script>

<template>
    <h1>Empty View</h1>
</template>
```

---
### File: src/views/ContactView.vue
---

```vue
<script setup lang="ts">

</script>

<template>
    <h1>Empty View</h1>
</template>
```

---
### File: src/views/HomeView.vue
---

```vue
<script setup lang="ts">
import HomeMarketTicker from '@/components/HomeMarketTicker.vue';

const getRarityGlowStyle = (rarity: string) => {
    const colors: Record<string, string> = {
        'COMMON': '#94a3b8',
        'UNCOMMON': '#34d399',
        'RARE': '#60a5fa',
        'EPIC': '#c084fc',
        'LEGENDARY': '#fbbf24'
    };
    const color = colors[rarity] || colors['COMMON'];
    return {
        boxShadow: `0 0 30px ${color}20`,
        borderColor: `${color}60`,
        color: color
    };
};
</script>

<template>
    <div
        class="w-screen max-w-[100vw] min-h-screen bg-slate-950 text-slate-200 font-sans overflow-x-hidden selection:bg-emerald-500/30">

        <header class="relative w-full pt-24 pb-12 phone:pt-32 phone:pb-20 lg:pt-48 lg:pb-32 overflow-hidden">

            <div
                class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full max-w-7xl opacity-30 pointer-events-none z-0">
                <div
                    class="absolute top-10 -right-20 phone:right-0 w-48 h-48 phone:w-96 phone:h-96 bg-emerald-500/30 rounded-full blur-[60px] phone:blur-[100px]">
                </div>
                <div
                    class="absolute bottom-10 -left-20 phone:left-0 w-40 h-40 phone:w-72 phone:h-72 bg-blue-600/20 rounded-full blur-[60px] phone:blur-[100px]">
                </div>
            </div>

            <div
                class="max-w-7xl mx-auto px-4 phone:px-12 grid lg:grid-cols-2 gap-12 items-center relative z-10 w-full">
                <div class="space-y-6 phone:space-y-8 text-center lg:text-left">

                    <div
                        class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-900 border border-slate-700/50 text-xs font-medium text-emerald-400 shadow-sm">
                        <span class="relative flex h-2 w-2">
                            <span
                                class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                        </span>
                        Closed Economy Alpha Live
                    </div>

                    <h1
                        class="text-4xl phone:text-5xl md:text-6xl lg:text-7xl font-bold leading-tight text-white break-words">
                        Cultivate your <br>
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-400">
                            Digital Paradise
                        </span>
                    </h1>

                    <p class="text-base phone:text-lg text-slate-400 max-w-xl mx-auto lg:mx-0 leading-relaxed">
                        Plant seeds, nurture rare flowers, and trade them in a fully player-driven economy.
                        Design your island and discover the secrets of botany in BloomScape.
                    </p>

                    <div class="flex flex-col phone:flex-row gap-4 justify-center lg:justify-start w-full">
                        <button
                            class="btn btn-lg w-full phone:w-auto bg-emerald-500 hover:bg-emerald-400 text-slate-900 border-none font-bold px-8 shadow-xl shadow-emerald-500/20 transition-all active:scale-95 hover:scale-105 hover:-translate-y-1">
                            Start Your Garden
                        </button>
                        <button
                            class="btn btn-lg w-full phone:w-auto btn-outline border-slate-700 text-slate-300 hover:text-white hover:bg-slate-800 hover:border-slate-600">
                            Explore Market
                        </button>
                    </div>

                    <div
                        class="pt-8 flex flex-col phone:flex-row items-center justify-center lg:justify-start gap-6 phone:gap-8 border-t border-slate-800/60 w-full">
                        <div class="text-center lg:text-left">
                            <div class="text-2xl font-bold text-white">12k+</div>
                            <div class="text-xs text-slate-500 uppercase tracking-wider font-bold">Active Plots</div>
                        </div>
                        <div class="text-center lg:text-left">
                            <div class="text-2xl font-bold text-white">850k</div>
                            <div class="text-xs text-slate-500 uppercase tracking-wider font-bold">Sap Traded</div>
                        </div>
                        <div class="text-center lg:text-left">
                            <div class="text-2xl font-bold text-white">142</div>
                            <div class="text-xs text-slate-500 uppercase tracking-wider font-bold">Species</div>
                        </div>
                    </div>
                </div>

                <div class="relative group perspective-1000 hidden lg:block w-full max-w-lg mx-auto">
                    <div
                        class="absolute inset-0 bg-gradient-to-tr from-emerald-500/20 to-cyan-500/20 rounded-3xl blur-3xl transform group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <div
                        class="relative bg-slate-900 border border-slate-700/80 rounded-2xl p-3 shadow-2xl transform rotate-y-12 rotate-x-6 transition-transform duration-500 group-hover:rotate-y-6 group-hover:rotate-x-3">
                        <div class="aspect-[4/3] bg-slate-950 rounded-xl overflow-hidden relative shadow-inner">
                            <div class="absolute inset-0"
                                style="background-image: linear-gradient(rgba(51, 65, 85, 0.3) 1px, transparent 1px), linear-gradient(90deg, rgba(51, 65, 85, 0.3) 1px, transparent 1px); background-size: 40px 40px; transform: scale(1.5) rotateX(45deg) rotateZ(45deg); opacity: 0.5;">
                            </div>
                            <div class="absolute inset-0 flex items-center justify-center">
                                <div class="relative">
                                    <div class="text-8xl filter drop-shadow-lg animate-float">
                                        <img src="/bloomscape_logo.png" width="100">
                                    </div>
                                </div>
                            </div>
                            <div class="absolute top-4 left-4 right-4 flex justify-between">
                                <div class="h-2 w-24 bg-slate-800 rounded-full overflow-hidden">
                                    <div class="h-full bg-emerald-500 w-2/3"></div>
                                </div>
                                <div
                                    class="px-2 py-0.5 bg-amber-500/20 text-amber-400 text-[10px] font-mono rounded border border-amber-500/20">
                                    5,420 Sap
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>

        <HomeMarketTicker class="w-full max-w-full" />

        <section class="py-16 phone:py-24 bg-slate-950 relative w-full overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 phone:px-6">
                <div class="text-center mb-12 phone:mb-16">
                    <h2 class="text-3xl phone:text-4xl font-bold text-white mb-4">Grow, Gather, Gain</h2>
                    <p class="text-slate-400 max-w-2xl mx-auto text-sm phone:text-base">
                        BloomScape isn't just about clicking flowers. It's a complex ecosystem where soil quality, water
                        levels, and real-time market trends determine your success.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 phone:gap-8">
                    <div
                        class="group p-6 phone:p-8 rounded-2xl bg-gradient-to-b from-slate-900 to-slate-900/50 border border-slate-800 hover:border-emerald-500/50 transition-all duration-300 hover:-translate-y-2 hover:shadow-xl hover:shadow-emerald-900/20">
                        <div
                            class="w-14 h-14 rounded-xl bg-emerald-500/10 text-emerald-400 flex items-center justify-center text-3xl mb-6 group-hover:scale-110 transition-transform">
                            💧
                        </div>
                        <h3 class="text-xl font-bold text-white mb-3 group-hover:text-emerald-300 transition-colors">
                            Dynamic Gardening</h3>
                        <p class="text-slate-400 text-sm leading-relaxed">
                            Every tile matters. Manage water levels and soil quality to boost the purity of your
                            flowers. Higher quality means higher selling prices.
                        </p>
                    </div>

                    <div
                        class="group p-6 phone:p-8 rounded-2xl bg-gradient-to-b from-slate-900 to-slate-900/50 border border-slate-800 hover:border-blue-500/50 transition-all duration-300 hover:-translate-y-2 hover:shadow-xl hover:shadow-blue-900/20">
                        <div
                            class="w-14 h-14 rounded-xl bg-blue-500/10 text-blue-400 flex items-center justify-center text-3xl mb-6 group-hover:scale-110 transition-transform">
                            📈
                        </div>
                        <h3 class="text-xl font-bold text-white mb-3 group-hover:text-blue-300 transition-colors">Live
                            Economy</h3>
                        <p class="text-slate-400 text-sm leading-relaxed">
                            The market never sleeps. Prices fluctuate based on player supply and demand. Buy low, sell
                            high, and try to corner the market.
                        </p>
                    </div>

                    <div
                        class="group p-6 phone:p-8 rounded-2xl bg-gradient-to-b from-slate-900 to-slate-900/50 border border-slate-800 hover:border-purple-500/50 transition-all duration-300 hover:-translate-y-2 hover:shadow-xl hover:shadow-purple-900/20">
                        <div
                            class="w-14 h-14 rounded-xl bg-purple-500/10 text-purple-400 flex items-center justify-center text-3xl mb-6 group-hover:scale-110 transition-transform">
                            🧬
                        </div>
                        <h3 class="text-xl font-bold text-white mb-3 group-hover:text-purple-300 transition-colors">
                            Genetics System</h3>
                        <p class="text-slate-400 text-sm leading-relaxed">
                            From Common daisies to Legendary void-flowers. Cross-breed species to discover secret
                            combinations and unlock value.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section class="py-20 phone:py-32 relative overflow-hidden bg-slate-900/30 border-y border-slate-800/50 w-full">
            <div class="max-w-7xl mx-auto px-6 relative z-10">
                <div class="flex flex-col md:flex-row items-center justify-between gap-12 phone:gap-16">

                    <div class="md:w-1/2 text-center md:text-left">
                        <h2 class="text-3xl phone:text-4xl font-bold text-white mb-6 leading-tight">
                            Collect the <span
                                class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-amber-400">Unattainable</span>
                        </h2>
                        <p class="text-slate-400 mb-8 text-base phone:text-lg leading-relaxed">
                            Some flowers are wild, others must be engineered. Will you be the first botanist to
                            stabilize the genome of the Legendary <span class="text-amber-400 font-bold">Solar
                                Lotus</span>?
                        </p>
                        <div class="space-y-4 max-w-md mx-auto md:mx-0 text-left">
                            <div
                                class="flex items-center gap-4 p-4 rounded-xl bg-slate-800/40 border border-slate-700/50">
                                <div
                                    class="w-10 h-10 rounded-full bg-emerald-500/10 flex items-center justify-center text-emerald-400 text-lg font-bold">
                                    1</div>
                                <h4 class="text-white font-bold text-sm">Harvest Seeds</h4>
                            </div>
                            <div
                                class="flex items-center gap-4 p-4 rounded-xl bg-slate-800/40 border border-slate-700/50">
                                <div
                                    class="w-10 h-10 rounded-full bg-blue-500/10 flex items-center justify-center text-blue-400 text-lg font-bold">
                                    2</div>
                                <h4 class="text-white font-bold text-sm">Cross-Breed</h4>
                            </div>
                            <div
                                class="flex items-center gap-4 p-4 rounded-xl bg-slate-800/40 border border-slate-700/50">
                                <div
                                    class="w-10 h-10 rounded-full bg-amber-500/10 flex items-center justify-center text-amber-400 text-lg font-bold">
                                    3</div>
                                <h4 class="text-white font-bold text-sm">Profit</h4>
                            </div>
                        </div>
                    </div>

                    <div
                        class="md:w-1/2 relative h-96 w-full flex items-center justify-center perspective-1000 scale-65 phone:scale-100">
                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-56 h-72 bg-slate-800 rounded-2xl border flex flex-col items-center justify-center transition-all duration-500 hover:translate-y-[-120px] hover:rotate-0 hover:z-30 cursor-pointer shadow-xl"
                            style="transform: translate(-60px, 10px) rotate(-12deg);"
                            :style="getRarityGlowStyle('EPIC')">
                            <div class="text-6xl mb-4 opacity-90">🌸</div>
                            <div class="font-bold text-purple-400">Lunar Orchid</div>
                            <div class="text-[10px] text-slate-500 mt-2 font-mono uppercase tracking-widest">EPIC</div>
                        </div>

                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-60 h-80 bg-slate-900 rounded-2xl border flex flex-col items-center justify-center shadow-2xl z-20 hover:scale-105 transition-all duration-300"
                            :style="getRarityGlowStyle('LEGENDARY')">
                            <div
                                class="absolute inset-0 bg-gradient-to-b from-amber-500/10 to-transparent rounded-2xl pointer-events-none">
                            </div>
                            <div class="text-7xl mb-6 drop-shadow-2xl filter brightness-110 animate-float">⚜️</div>
                            <div class="font-bold text-amber-400 text-2xl font-serif">Golden Rose</div>
                            <div
                                class="mt-4 px-3 py-1 bg-amber-500/10 border border-amber-500/30 rounded text-[10px] text-amber-300 font-bold tracking-[0.2em]">
                                LEGENDARY</div>
                        </div>

                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-56 h-72 bg-slate-800 rounded-2xl border flex flex-col items-center justify-center transition-all duration-500 hover:translate-y-[-120px] hover:rotate-0 hover:z-30 cursor-pointer shadow-xl"
                            style="transform: translate(60px, 10px) rotate(12deg);" :style="getRarityGlowStyle('RARE')">
                            <div class="text-6xl mb-4 opacity-90">🌺</div>
                            <div class="font-bold text-blue-400">Frost Hibiscus</div>
                            <div class="text-[10px] text-slate-500 mt-2 font-mono uppercase tracking-widest">RARE</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </div>
</template>

<style scoped>
/* Page-specific animations */
@keyframes float {

    0%,
    100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-10px);
    }
}

.animate-float {
    animation: float 4s ease-in-out infinite;
}

.perspective-1000 {
    perspective: 1000px;
}

.rotate-y-12 {
    transform: rotateY(-12deg) rotateX(5deg);
}
</style>
```

---
### File: src/views/WikiView.vue
---

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'
import { FlowerRarity } from '@/shared/types'

// --- NAVIGATION STATE ---
type WikiCategory = 'OVERVIEW' | 'TOOLS' | 'ECONOMY' | 'MECHANICS'
const activeCategory = ref<WikiCategory>('OVERVIEW')
const searchQuery = ref('')

// --- MOCK DATA ---

const itemDatabase = [
    { name: 'Rusty Can', type: 'Tool', desc: 'Basic watering can. Holds 10L.', cost: 'Free' },
    { name: 'Cloud Sprinkler', type: 'Tool', desc: 'Automatically waters a 3x3 area.', cost: '5,000 Sap' },
    { name: 'Nutrient Mix', type: 'Consumable', desc: 'Instantly restores soil quality by 20%.', cost: '200 Sap' },
    { name: 'Genetic Analyzer', type: 'Tool', desc: 'Reveals hidden genes of a seed before planting.', cost: '1,500 Sap' },
]

const mechanics = [
    {
        title: 'Soil Quality',
        content: 'Soil quality starts at 100% and degrades by 10% after every harvest. Low quality soil increases the chance of "Withered" flowers. Use Fertilizer to restore it.'
    },
    {
        title: 'Cross-Breeding',
        content: 'Planting two different species next to each other gives a 15% chance to spawn a hybrid seed in an adjacent empty tile. Hybrids often possess higher rarity traits.'
    },
    {
        title: 'Market Fluctuations',
        content: 'Prices update every 4 hours based on global player sales. If everyone sells Moon Roses, their value drops. Scarcity drives profit.'
    }
]

// --- HELPERS ---

const getRarityColor = (rarity: string) => {
    switch (rarity) {
        case 'COMMON': return 'text-slate-400 bg-slate-400/10 border-slate-400/20';
        case 'UNCOMMON': return 'text-emerald-400 bg-emerald-400/10 border-emerald-400/20';
        case 'RARE': return 'text-blue-400 bg-blue-400/10 border-blue-400/20';
        case 'EPIC': return 'text-purple-400 bg-purple-400/10 border-purple-400/20';
        case 'LEGENDARY': return 'text-amber-400 bg-amber-400/10 border-amber-400/20';
        default: return 'text-slate-400';
    }
}

</script>

<template>
    <div class="w-screen min-h-screen bg-slate-950 text-slate-200 flex flex-col lg:flex-row">

        <aside
            class="w-full lg:w-64 bg-slate-900 border-r border-slate-800 flex-shrink-0 lg:h-[calc(100vh-64px)] lg:sticky lg:top-16 overflow-y-auto">
            <div class="p-6">
                <h2 class="text-xs font-bold text-slate-500 uppercase tracking-widest mb-4">Wiki Navigation</h2>
                <nav class="space-y-1">
                    <button @click="activeCategory = 'OVERVIEW'"
                        class="w-full text-left px-4 py-2 rounded-lg text-sm font-medium transition-colors"
                        :class="activeCategory === 'OVERVIEW' ? 'bg-emerald-500/10 text-emerald-400' : 'text-slate-400 hover:text-white hover:bg-slate-800'">
                        Overview
                    </button>
                    <button @click="activeCategory = 'TOOLS'"
                        class="w-full text-left px-4 py-2 rounded-lg text-sm font-medium transition-colors"
                        :class="activeCategory === 'TOOLS' ? 'bg-blue-500/10 text-blue-400' : 'text-slate-400 hover:text-white hover:bg-slate-800'">
                        Items & Tools
                    </button>
                    <button @click="activeCategory = 'MECHANICS'"
                        class="w-full text-left px-4 py-2 rounded-lg text-sm font-medium transition-colors"
                        :class="activeCategory === 'MECHANICS' ? 'bg-purple-500/10 text-purple-400' : 'text-slate-400 hover:text-white hover:bg-slate-800'">
                        Game Mechanics
                    </button>
                    <button @click="activeCategory = 'ECONOMY'"
                        class="w-full text-left px-4 py-2 rounded-lg text-sm font-medium transition-colors"
                        :class="activeCategory === 'ECONOMY' ? 'bg-amber-500/10 text-amber-400' : 'text-slate-400 hover:text-white hover:bg-slate-800'">
                        Economy Guide
                    </button>
                </nav>
            </div>

            <div class="px-6 pb-6 mt-auto">
                <div class="bg-slate-800/50 p-4 rounded-xl border border-slate-700/50">
                    <div class="text-xs font-bold text-emerald-400 mb-1">💡 Pro Tip</div>
                    <p class="text-xs text-slate-400">
                        Watering flowers at night reduces evaporation by 30%.
                    </p>
                </div>
            </div>
        </aside>

        <main class="flex-1 p-6 lg:p-10 overflow-y-auto">

            <div
                class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8 pb-8 border-b border-slate-800">
                <div>
                    <h1 class="text-3xl font-bold text-white mb-2">
                        {{ activeCategory === 'OVERVIEW' ? 'Welcome to BloomScape' :
                            activeCategory === 'TOOLS' ? 'Equipment & Items' :
                                activeCategory === 'MECHANICS' ? 'Advanced Mechanics' : 'Economic Theory' }}
                    </h1>
                    <p class="text-slate-400">The official guide to cultivating your digital paradise.</p>
                </div>
            </div>

            <div v-if="activeCategory === 'OVERVIEW'" class="space-y-8 animate-fade-in">
                <div class="prose prose-invert max-w-none">
                    <p class="text-lg leading-relaxed text-slate-300">
                        BloomScape is a <strong>real-time gardening simulation</strong> connected to a live player
                        economy.
                        Your goal is to transform a barren island into a thriving nursery, discover rare genetic
                        variants,
                        and amass a fortune in <span class="text-emerald-400 font-mono">Sap</span>.
                    </p>
                </div>

                <div class="grid md:grid-cols-3 gap-6">
                    <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 hover:border-blue-500/30 transition-colors cursor-pointer"
                        @click="activeCategory = 'TOOLS'">
                        <div class="text-4xl mb-4">💧</div>
                        <h3 class="font-bold text-white mb-2">Mastering Tools</h3>
                        <p class="text-sm text-slate-400">From rusty cans to automated irrigation systems.</p>
                    </div>
                    <div class="bg-slate-900 p-6 rounded-xl border border-slate-800 hover:border-amber-500/30 transition-colors cursor-pointer"
                        @click="activeCategory = 'ECONOMY'">
                        <div class="text-4xl mb-4">🪙</div>
                        <h3 class="font-bold text-white mb-2">Making Profit</h3>
                        <p class="text-sm text-slate-400">Understanding supply, demand, and market crashes.</p>
                    </div>
                </div>
            </div>

            <div v-if="activeCategory === 'TOOLS'" class="animate-fade-in">
                <div class="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden">
                    <table class="w-full text-left">
                        <thead class="bg-slate-950 text-xs uppercase text-slate-500">
                            <tr>
                                <th class="px-6 py-4 font-bold">Item Name</th>
                                <th class="px-6 py-4 font-bold">Type</th>
                                <th class="px-6 py-4 font-bold">Description</th>
                                <th class="px-6 py-4 font-bold text-right">Cost</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800">
                            <tr v-for="item in itemDatabase" :key="item.name"
                                class="hover:bg-slate-800/50 transition-colors">
                                <td class="px-6 py-4 font-bold text-white">{{ item.name }}</td>
                                <td class="px-6 py-4">
                                    <span
                                        class="text-xs px-2 py-1 rounded bg-slate-800 border border-slate-700 text-slate-300">
                                        {{ item.type }}
                                    </span>
                                </td>
                                <td class="px-6 py-4 text-sm text-slate-400">{{ item.desc }}</td>
                                <td class="px-6 py-4 text-right font-mono text-emerald-400">{{ item.cost }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div v-if="activeCategory === 'MECHANICS'" class="animate-fade-in space-y-6">
                <div v-for="(mech, i) in mechanics" :key="i"
                    class="bg-slate-900 p-6 rounded-xl border border-slate-800">
                    <h3 class="text-xl font-bold text-purple-400 mb-3 flex items-center gap-2">
                        <span
                            class="text-sm bg-purple-500/10 px-2 py-1 rounded text-purple-400 border border-purple-500/20">0{{
                                i + 1 }}</span>
                        {{ mech.title }}
                    </h3>
                    <p class="text-slate-300 leading-relaxed">{{ mech.content }}</p>
                </div>
            </div>

            <div v-if="activeCategory === 'ECONOMY'" class="animate-fade-in">
                <div class="bg-slate-900 border border-slate-800 rounded-xl p-8 text-center">
                    <div class="text-6xl mb-6">📉 📈</div>
                    <h2 class="text-2xl font-bold text-white mb-4">The Closed Economy</h2>
                    <div class="prose prose-invert max-w-2xl mx-auto text-left">
                        <p>
                            BloomScape operates on a <strong>closed economy model</strong>. This means the game server
                            does not buy flowers infinitely.
                            If you sell a flower, another player (or a limited NPC collector) must buy it.
                        </p>
                        <ul class="list-disc pl-5 space-y-2 mt-4 text-slate-400">
                            <li><strong>Sap</strong> is generated by completing daily quests and selling to NPCs.</li>
                            <li><strong>Inflation</strong> is controlled by land taxes and tool degradation.</li>
                            <li><strong>Prices</strong> are determined by the average of the last 24h of
                                player-to-player trades.</li>
                        </ul>
                    </div>
                </div>
            </div>

        </main>
    </div>
</template>

<style scoped>
.animate-fade-in {
    animation: fadeIn 0.3s ease-out forwards;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Custom Scrollbar for Sidebar */
aside::-webkit-scrollbar {
    width: 6px;
}

aside::-webkit-scrollbar-track {
    background: transparent;
}

aside::-webkit-scrollbar-thumb {
    background-color: #334155;
    border-radius: 20px;
}
</style>
```

---
### File: src/views/admin/DBManagerView.vue
---

```vue
<script setup lang="ts">
import { AdminController } from '@/server/controllers/AdminController';

</script>

<template>
    <button @click="AdminController.populateMarket()" class="btn btn-primary">Seed DB</button>
</template>
```

---
### File: src/views/admin/ManagerView.vue
---

```vue
<script setup lang="ts">

import AdminSideBar, { MenuItem } from '@/components/admin/AdminSideBar.vue'

import AdminConfig from '@/components/admin/integrated_views/AdminConfig.vue'
import AdminDatabase from '@/components/admin/integrated_views/AdminDatabase.vue'
import AdminLogs from '@/components/admin/integrated_views/AdminLogs.vue'
import AdminModeration from '@/components/admin/integrated_views/AdminModeration.vue'
import AdminOverview from '@/components/admin/integrated_views/AdminOverview.vue'
import AdminReports from '@/components/admin/integrated_views/AdminReports.vue'
import AdminUsers from '@/components/admin/integrated_views/AdminUsers.vue'

import { ref, computed } from 'vue'

// --- NAVIGATION CONFIG ---
const activeTabId = ref('OVERVIEW')

const menuItems: MenuItem[] = [
    { id: 'OVERVIEW', label: 'Stats & Analytics' },
    { id: 'MODERATION', label: 'Moderation Queue' },
    { id: 'REPORTS', label: 'Player Reports' },
    { id: 'USERS', label: 'User Management' },
    { id: 'DATABASE', label: 'Database Editor' },
    { id: 'CONFIG', label: 'Game Config' },
    { id: 'LOGS', label: 'System Logs' }
]

// Dynamic Component Lookup
const currentView = computed(() => {
    switch (activeTabId.value) {
        case 'OVERVIEW': return AdminOverview
        case 'MODERATION': return AdminModeration
        case 'REPORTS': return AdminReports
        case 'USERS': return AdminUsers
        case 'DATABASE': return AdminDatabase
        case 'CONFIG': return AdminConfig
        case 'LOGS': return AdminLogs
        default: return AdminOverview
    }
})

const activeTitle = computed(() =>
    menuItems.find(i => i.id === activeTabId.value)?.label ?? 'Admin'
)
</script>

<template>
    <div class="w-screen min-h-screen bg-slate-950 text-slate-200 flex font-sans">

        <AdminSideBar :active-tab="activeTabId" :menu-items="menuItems" @update:tab="(id) => activeTabId = id" />

        <main class="flex-1 ml-64 p-8 bg-slate-950 min-h-screen">
            <header class="flex justify-between items-center mb-8 pb-4 border-b border-slate-800">
                <h1 class="text-2xl font-bold text-white">
                    {{ activeTitle }}
                </h1>
            </header>

            <Transition name="fade" mode="out-in">
                <component :is="currentView" />
            </Transition>
        </main>
    </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
```

---
### File: src/views/errors/404View.vue
---

```vue
<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();
</script>

<template>
    <div class="w-screen min-h-[50vw] bg-slate-950 relative flex items-center justify-center overflow-hidden font-sans">

        <div class="absolute inset-0 pointer-events-none">
            <div
                class="absolute -top-1/2 -left-1/2 w-[200%] h-[200%] bg-[radial-gradient(circle,rgba(16,185,129,0.1)_0%,transparent_60%)] animate-drift-slow opacity-60">
            </div>
            <div
                class="absolute top-0 left-0 w-full h-full bg-[radial-gradient(ellipse_at_bottom,rgba(15,23,42,0.8)_0%,transparent_70%)]">
            </div>
            <div class="particle p1"></div>
            <div class="particle p2"></div>
            <div class="particle p3"></div>
        </div>

        <div class="relative z-10 text-center px-6">

            <div class="mb-8 flex justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"
                    class="w-48 h-48 text-emerald-500/80 drop-shadow-[0_0_15px_rgba(16,185,129,0.4)] animate-float">
                    <path fill="currentColor" d="M100 160l-60-30v-40l60-30 60 30v40z" class="text-slate-800" />
                    <path fill="currentColor" d="M40 90l60 30 60-30-60-30z" class="text-slate-700" />
                    <path fill="currentColor" d="M110 60l20-10 10 20-20 10z" class="text-slate-600 animate-pulse-slow"
                        style="animation-delay: 0.5s" />
                    <path fill="currentColor" d="M60 100l-20 10-10-20 20-10z"
                        class="text-slate-600 animate-pulse-slow" />
                    <path fill="currentColor" d="M140 130l15-5 5 15-15 5z" class="text-slate-700 animate-pulse-slow"
                        style="animation-delay: 1s" />
                    <path stroke="currentColor" stroke-width="3" stroke-linecap="round" fill="none"
                        d="M100 70l-10 20 15 10-20 30 5 15" class="text-emerald-400" />
                </svg>
            </div>

            <h1
                class="text-8xl md:text-9xl font-black text-transparent bg-clip-text bg-gradient-to-b from-emerald-400 via-emerald-600 to-slate-900 drop-shadow-2xl">
                404
            </h1>

            <h2 class="text-2xl md:text-3xl font-bold text-white mt-6 tracking-wide uppercase">
                Uncharted Territory
            </h2>

            <p class="text-slate-400 mt-4 max-w-md mx-auto text-lg leading-relaxed">
                You've sailed past the known world. This island seems to have crumbled into the void, or perhaps it
                never existed on our charts at all.
            </p>

            <div class="flex flex-col sm:flex-row gap-4 mt-10 justify-center">
                <button @click="router.push('/')"
                    class="btn bg-emerald-600 hover:bg-emerald-500 text-white border-none font-bold px-8 shadow-lg shadow-emerald-900/50 group relative overflow-hidden">
                    <span class="relative z-10">Return to Safety</span>
                    <div
                        class="absolute inset-0 h-full w-full scale-0 rounded-lg transition-all duration-300 group-hover:scale-100 group-hover:bg-white/10">
                    </div>
                </button>

                <button @click="router.go(-1)" class="btn btn-ghost text-slate-300 hover:text-white hover:bg-slate-800">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                        stroke="currentColor" class="w-4 h-4 mr-2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
                    </svg>
                    Go Back
                </button>
            </div>

        </div>
    </div>
</template>

<style scoped>
/* Custom animations not provided by default Tailwind */

/* Floating effect for the main icon */
@keyframes float {

    0%,
    100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-15px);
    }
}

.animate-float {
    animation: float 6s ease-in-out infinite;
}

/* Slow pulse for broken parts */
@keyframes pulse-slow {

    0%,
    100% {
        opacity: 0.6;
        transform: scale(1);
    }

    50% {
        opacity: 1;
        transform: scale(1.05);
    }
}

.animate-pulse-slow {
    animation: pulse-slow 4s ease-in-out infinite;
}

/* Background fog drifting */
@keyframes drift {
    0% {
        transform: translate(0, 0) rotate(0deg);
    }

    50% {
        transform: translate(-5%, -5%) rotate(2deg);
    }

    100% {
        transform: translate(0, 0) rotate(0deg);
    }
}

.animate-drift-slow {
    animation: drift 30s ease-in-out infinite;
}

/* Tiny floating particles in background */
.particle {
    position: absolute;
    border-radius: 50%;
    background: rgba(16, 185, 129, 0.3);
    /* Emeraldish */
    animation: float-up linear infinite;
}

.p1 {
    width: 4px;
    height: 4px;
    left: 20%;
    bottom: -10px;
    animation-duration: 15s;
}

.p2 {
    width: 6px;
    height: 6px;
    left: 60%;
    bottom: -20px;
    animation-duration: 20s;
    animation-delay: 2s;
    opacity: 0.2;
}

.p3 {
    width: 3px;
    height: 3px;
    left: 80%;
    bottom: -10px;
    animation-duration: 12s;
    animation-delay: 5s;
}

@keyframes float-up {
    0% {
        transform: translateY(0) translateX(0);
        opacity: 0;
    }

    10% {
        opacity: 0.5;
    }

    90% {
        opacity: 0.5;
    }

    100% {
        transform: translateY(-100vh) translateX(20px);
        opacity: 0;
    }
}
</style>
```

---
### File: src/views/game/FloraDexView.vue
---

```vue
<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { GameController } from '@/server/controllers/GameController'
import { DiscoverySource, FlowerRarity } from '@/shared/types'
import FlowerImage from '@/components/FlowerImage.vue'

// Updated Interface
interface FloradexEntry {
    id: string
    name: string
    slugName: string
    description: string
    rarity: FlowerRarity
    discovered: boolean
    discoveryDate?: string
    discoverySource?: typeof DiscoverySource[keyof typeof DiscoverySource]
    initialQuality?: number
}

const floradex = ref<FloradexEntry[]>([])
const isLoading = ref(true)
const searchQuery = ref('')
const sortOption = ref<'RARITY_DESC' | 'RARITY_ASC' | 'NAME_ASC' | 'DISCOVERED' | 'DATE_DESC'>('RARITY_DESC')

const RARITY_WEIGHT: Record<string, number> = {
    'LEGENDARY': 5,
    'EPIC': 4,
    'RARE': 3,
    'UNCOMMON': 2,
    'COMMON': 1
}

const stats = computed(() => {
    const total = floradex.value.length
    const found = floradex.value.filter(f => f.discovered).length
    return { total, found, percent: total > 0 ? Math.round((found / total) * 100) : 0 }
})

const processedFloradex = computed(() => {
    let list = [...floradex.value]

    if (searchQuery.value) {
        const q = searchQuery.value.toLowerCase()
        list = list.filter(f => f.name.toLowerCase().includes(q))
    }

    return list.sort((a, b) => {
        switch (sortOption.value) {
            case 'NAME_ASC':
                return a.name.localeCompare(b.name)
            case 'RARITY_ASC':
                return (RARITY_WEIGHT[a.rarity] - RARITY_WEIGHT[b.rarity]) || a.name.localeCompare(b.name)
            case 'RARITY_DESC':
                return (RARITY_WEIGHT[b.rarity] - RARITY_WEIGHT[a.rarity]) || a.name.localeCompare(b.name)
            case 'DISCOVERED':
                if (a.discovered === b.discovered) return 0;
                return a.discovered ? -1 : 1;
            case 'DATE_DESC':
                const dateA = a.discoveryDate ? new Date(a.discoveryDate).getTime() : 0;
                const dateB = b.discoveryDate ? new Date(b.discoveryDate).getTime() : 0;
                return dateB - dateA;
            default: return 0
        }
    })
})

const fetchFloradex = async () => {
    isLoading.value = true
    try {
        floradex.value = await GameController.getFloradex() as any
    } catch (e) {
        console.error(e)
    } finally {
        isLoading.value = false
    }
}

onMounted(fetchFloradex)

const getRarityColor = (rarity: FlowerRarity) => {
    const colors: Record<string, string> = {
        'COMMON': 'text-slate-400 border-slate-700',
        'UNCOMMON': 'text-emerald-400 border-emerald-500/50',
        'RARE': 'text-blue-400 border-blue-500/50',
        'EPIC': 'text-purple-400 border-purple-500/50',
        'LEGENDARY': 'text-amber-400 border-amber-500/50'
    }
    return colors[rarity] || colors['COMMON']
}

const getRarityBg = (rarity: FlowerRarity) => {
    const colors: Record<string, string> = {
        'COMMON': 'bg-slate-800/50',
        'UNCOMMON': 'bg-emerald-900/20',
        'RARE': 'bg-blue-900/20',
        'EPIC': 'bg-purple-900/20',
        'LEGENDARY': 'bg-amber-900/20'
    }
    return colors[rarity] || 'bg-slate-800/50'
}

// Helper to format source nicely
const getSourceLabel = (source?: string) => {
    switch (source) {
        case 'WILD': return 'Found in Wild';
        case 'BREEDING': return 'Cross-Bred';
        case 'MARKET': return 'Bought';
        case 'GIFT': return 'Gifted';
        default: return 'Unknown';
    }
}
</script>

<template>
    <div class="w-screen min-h-screen bg-slate-950 text-slate-200 p-6 pb-20">

        <div class="max-w-7xl mx-auto">
            <div class="flex flex-col lg:flex-row items-end lg:items-center justify-between mb-8 gap-6">
                <div class="w-full lg:w-auto ml-5">
                    <h1
                        class="text-4xl font-bold text-white mb-2 flex items-center justify-center lg:justify-start gap-3">
                        FloraDex
                    </h1>
                    <p class="text-slate-400 flex justify-center lg:justify-start">Track your botanical discoveries.</p>
                </div>

                <div
                    class="w-full lg:w-auto flex flex-col sm:flex-row gap-4 bg-slate-900/80 p-2 rounded-xl border border-slate-800 backdrop-blur-sm">
                    <div class="relative flex-1 sm:w-100">
                        <span class="absolute left-3 top-2.5 text-slate-500 text-xs">🔍</span>
                        <input v-model="searchQuery" type="text" placeholder="Search species..."
                            class="input input-sm w-full min-w-20 bg-slate-950 border-slate-700 focus:border-emerald-500 text-slate-200" />
                    </div>

                    <select v-model="sortOption"
                        class="select select-sm bg-slate-950 border-slate-700 text-slate-200 focus:border-emerald-500">
                        <option value="RARITY_DESC">Rarity (High to Low)</option>
                        <option value="RARITY_ASC">Rarity (Low to High)</option>
                        <option value="NAME_ASC">Name (A-Z)</option>
                        <option value="DATE_DESC">Date Discovered</option>
                        <option value="DISCOVERED">Discovered Status</option>
                    </select>
                </div>
            </div>

            <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-800 w-full mb-8">
                <div class="flex justify-between text-sm mb-2">
                    <span class="text-slate-400 font-medium">Collection Progress</span>
                    <span class="text-emerald-400 font-bold font-mono">{{ stats.found }} / {{ stats.total }}</span>
                </div>
                <div class="w-full h-3 bg-slate-800 rounded-full overflow-hidden">
                    <div class="h-full bg-gradient-to-r from-emerald-600 to-emerald-400 transition-all duration-1000 ease-out"
                        :style="{ width: `${stats.percent}%` }"></div>
                </div>
            </div>

            <div v-if="isLoading" class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-6">
                <div v-for="i in 10" :key="i" class="h-64 bg-slate-900 rounded-xl animate-pulse"></div>
            </div>

            <div v-else class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">

                <div v-for="flower in processedFloradex" :key="flower.id"
                    class="group relative bg-slate-900 rounded-xl border overflow-hidden transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
                    :class="flower.discovered ? getRarityBg(flower.rarity) + ' ' + getRarityColor(flower.rarity) : 'border-slate-800 bg-slate-900'">

                    <div v-if="flower.discovered"
                        class="absolute top-3 right-3 z-10 px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider bg-slate-950/80 backdrop-blur border border-white/10 shadow-sm">
                        {{ flower.rarity }}
                    </div>

                    <div class="aspect-square relative p-6 flex items-center justify-center bg-slate-950/30">
                        <FlowerImage :slug="flower.slugName" status="MATURE" type="icon" size="100%"
                            class="transition-all duration-500"
                            :class="flower.discovered
                                ? 'drop-shadow-[0_4px_6px_rgba(0,0,0,0.5)] group-hover:scale-110'
                                : 'brightness-0 opacity-20 grayscale blur-[2px] group-hover:blur-0 group-hover:opacity-40'" />

                        <div v-if="!flower.discovered"
                            class="absolute inset-0 flex items-center justify-center pointer-events-none">
                            <div
                                class="w-10 h-10 rounded-full bg-slate-800/80 backdrop-blur flex items-center justify-center text-slate-500 border border-slate-700">
                                🔒
                            </div>
                        </div>
                    </div>

                    <div class="p-4 border-t border-white/5 flex flex-col h-full">
                        <div v-if="flower.discovered">
                            <h3 class="font-bold text-white truncate">{{ flower.name }}</h3>
                            <p class="text-xs text-white/50 line-clamp-2 mt-1 mb-2 min-h-[2.5em]">{{ flower.description
                                }}</p>

                            <div class="mt-auto pt-2 border-t border-white/5 space-y-1">
                                <div class="flex justify-between items-center text-[10px] text-slate-400">
                                    <span class="uppercase tracking-wider">Date</span>
                                    <span class="font-mono text-slate-200">
                                        {{ flower.discoveryDate ? new Date(flower.discoveryDate).toLocaleDateString() :
                                            '-' }}
                                    </span>
                                </div>
                                <div class="flex justify-between items-center text-[10px] text-slate-400">
                                    <span class="uppercase tracking-wider">Source</span>
                                    <span class="text-emerald-400 font-bold">
                                        {{ getSourceLabel(flower.discoverySource) }}
                                    </span>
                                </div>
                            </div>
                        </div>
                        <div v-else>
                            <h3 class="font-bold text-slate-600">Unknown Species</h3>
                            <p class="text-xs text-slate-700 mt-1">Discover this flower to unlock its data.</p>
                        </div>
                    </div>
                </div>

                <div v-if="!searchQuery"
                    class="relative bg-slate-950 rounded-xl border border-slate-800 border-dashed flex flex-col items-center justify-center text-center p-6 group cursor-help overflow-hidden min-h-[250px]">
                    <div
                        class="absolute inset-0 bg-gradient-to-br from-purple-900/10 to-blue-900/10 opacity-0 group-hover:opacity-100 transition-opacity">
                    </div>
                    <div class="relative z-10 transform transition-transform group-hover:scale-110 duration-500">
                        <div
                            class="text-6xl mb-4 opacity-30 group-hover:opacity-100 transition-opacity filter blur-[1px] group-hover:blur-0">
                            🧬
                        </div>
                    </div>
                    <div class="relative z-10">
                        <h3 class="font-bold text-slate-500 group-hover:text-purple-400 transition-colors">Secret
                            Variations</h3>
                        <p class="text-xs text-slate-600 mt-2 group-hover:text-slate-400 transition-colors">
                            Rare mutations & event exclusives hide in the shadows.
                        </p>
                    </div>
                </div>

                <div v-if="processedFloradex.length === 0 && searchQuery"
                    class="col-span-full py-12 text-center text-slate-500 italic">
                    No flowers found matching "{{ searchQuery }}"
                </div>

            </div>
        </div>
    </div>
</template>

<style scoped>
.brightness-0 {
    filter: brightness(0);
}
</style>
```

---
### File: src/views/game/LandView.vue
---

```vue
<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import LandScene from '@/components/game/LandScene.vue';
import SideBar from '@/components/game/SideBar.vue';
import TopBar from '@/components/game/TopBar.vue';
import { useGameStore } from '@/stores/game';
import { useAuthStore } from '@/stores/auth';
import { useRoute } from 'vue-router';
import { UserController } from '@/server/controllers/UserController';

const gameStore = useGameStore();
const auth = useAuthStore();
const route = useRoute();
const userId = ref<string | null>(null);

onMounted(async () => {
    await auth.fetchSessionUser();
    userId.value = route.params.tag
        ? (await UserController.getUserByTag(route.params.tag as string)).user.id
        : auth.user?.id;
});

const formatCoord = (n: number) => n.toString().padStart(2, '0');
const activeTile = computed(() => gameStore.selectedTile || gameStore.hoveredTile);

</script>

<template>
    <div class="relative w-screen h-screen overflow-hidden bg-slate-900 text-slate-200 z-0">

        <LandScene v-if="userId" quality="high" :user-id="userId" />

        <div v-else class="absolute inset-0 flex items-center justify-center text-slate-500 z-0">
            <p>Rendering engine is out of fertilizer. If you just logged in, <b><button
                        onclick="window.location.reload()">reload</button></b> the page :)</p>
        </div>

        <div class="absolute inset-0 z-10 pointer-events-none">
            <SideBar />
            <TopBar :user-tag="route.params.tag || auth.user?.tag || ''" />

            <transition name="slide-up">
                <div v-if="activeTile" class="absolute bottom-8 right-8 pointer-events-auto">
                    <div class="card w-72 glass-card shadow-2xl border-t border-white/10">
                        <div class="card-body p-5">

                            <div class="flex justify-between items-start mb-2">
                                <div>
                                    <h2 class="card-title text-base font-bold" :class="{
                                        'text-emerald-300': activeTile.isOwned,
                                        'text-slate-400': !activeTile.isOwned
                                    }">
                                        {{ activeTile.isOwned ? 'Occupied Slot' : 'International Waters' }}
                                    </h2>
                                    <span class="text-xs font-mono text-slate-400">
                                        X:{{ formatCoord(activeTile.x) }} | Z:{{ formatCoord(activeTile.z) }}
                                    </span>
                                </div>
                                <div class="badge badge-xs"
                                    :class="activeTile.isOwned ? 'badge-success' : 'badge-ghost'">
                                    {{ activeTile.isOwned ? 'OWNED' : 'WILD' }}
                                </div>
                            </div>

                            <div class="text-xs text-slate-300 flex flex-col gap-2 my-2">
                                <p v-if="activeTile.isOwned">
                                    Occupied Land.
                                    <span v-if="gameStore.selectedEntity?.createdAt">
                                        Founded on {{ new Date(gameStore.selectedEntity.createdAt).toLocaleDateString()
                                        }}.
                                    </span>
                                </p>
                                <p v-else>
                                    Wild waters. Expand your territory here.
                                </p>
                            </div>

                            <div class="card-actions justify-end mt-2 pt-4 border-t border-white/5"
                                v-if="gameStore.selectedTile">

                                <button v-if="activeTile.isOwned"
                                    class="btn btn-sm btn-primary w-full text-white shadow-lg shadow-emerald-500/20">
                                    Manage
                                </button>

                                <button v-else-if="!activeTile.isOwned && activeTile.isAdjacentToLand"
                                    @click="gameStore.buyTile(activeTile.x, activeTile.z)"
                                    :disabled="gameStore.isLoading"
                                    class="btn btn-sm btn-outline btn-accent w-full group">

                                    <span v-if="gameStore.isLoading">Processing...</span>
                                    <span v-else>
                                        Buy Plot <span class="group-hover:translate-x-1 transition-transform">→</span>
                                    </span>
                                </button>

                                <button v-else-if="!activeTile.isOwned" disabled
                                    class="btn btn-sm btn-disabled w-full opacity-50 cursor-not-allowed">
                                    Too far from land
                                </button>

                            </div>

                        </div>
                    </div>
                </div>
            </transition>

        </div>
    </div>
</template>

<style scoped>
.glass-card {
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}

.slide-up-enter-active,
.slide-up-leave-active {
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-up-enter-from,
.slide-up-leave-to {
    transform: translateY(40px) scale(0.95);
    opacity: 0;
}
</style>
```

---
### File: src/views/game/LeaderboardView.vue
---

```vue

```

---
### File: src/views/game/MarketView.vue
---

```vue
<script setup lang="ts">
import MarketInModal from '@/components/game/modal_features/MarketInModal.vue';

</script>

<template>
    <MarketInModal></MarketInModal>
</template>
```

---
### File: src/views/game/UserProfileView.vue
---

```vue
<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { UserController } from '@/server/controllers/UserController';
import { GameController } from '@/server/controllers/GameController';
import { User } from '@/shared/user/User';
import { Role, FlowerRarity } from '@/shared/types';
import { ROUTES_ENUM as ROUTES } from '@/routes/routes_enum';

const route = useRoute();
const router = useRouter();
const auth = useAuthStore();

// --- STATE ---
const isLoading = ref(true);
const user = ref<User | null>(null);
const hasIsland = ref(false);
const userInventory = ref<any>(null);
const achievements = ref<any[]>([]); // Real data
const stats = ref({
    joinedAt: '',
    completionRate: 0,
});

// --- COMPUTED ---
const isOwnProfile = computed(() => (auth.user?.tag === route.params.tag) || (!route.params.tag && auth.user));

const levelProgress = computed(() => {
    if (!user.value) return 0;
    return Math.min(100, (user.value.xp / (user.value.level * 1000)) * 100);
});

// --- ACTIONS ---
async function fetchUserProfile() {
    isLoading.value = true
    let targetTag = route.params.tag as string

    if (!targetTag) {
        targetTag = auth.user?.tag || ''
    }

    // Safety check if direct access without auth
    if (!targetTag && !auth.user) {
        router.push(ROUTES.LOGIN.path);
        return;
    }

    try {
        const res = await UserController.getUserByTag(targetTag)

        if (res && res.user) {
            user.value = res.user
            stats.value.joinedAt = new Date(res.user.createdAt!).toLocaleDateString()

            // Parallel fetching for performance
            const [islandDetails, achievementList] = await Promise.all([
                GameController.getIslandDetails(res.user.id),
                GameController.getUserAchievements(res.user.id)
            ]);

            hasIsland.value = !!islandDetails
            achievements.value = achievementList

            // Mock Inventory (replace with real Controller call when ready)
            userInventory.value = {
                bestFlower: { name: 'Void Tulip', rarity: FlowerRarity.RARE }
            }
        } else {
            router.push({ name: ROUTES.NOT_FOUND.name })
        }
    } catch (e) {
        console.error(e)
        router.push(ROUTES.HOME.path)
    } finally {
        isLoading.value = false
    }
}

function getRarityColor(rarity: FlowerRarity | string) {
    const colors: Record<string, string> = {
        [FlowerRarity.COMMON]: 'text-slate-400 bg-slate-800',
        [FlowerRarity.UNCOMMON]: 'text-emerald-400 bg-emerald-900/30 border-emerald-500/30',
        [FlowerRarity.RARE]: 'text-blue-400 bg-blue-900/30 border-blue-500/30',
        [FlowerRarity.EPIC]: 'text-purple-400 bg-purple-900/30 border-purple-500/30',
        [FlowerRarity.LEGENDARY]: 'text-amber-400 bg-amber-900/30 border-amber-500/30'
    };
    return colors[rarity] || colors[FlowerRarity.COMMON];
}

function navigateToLand() {
    if (!user.value) return;
    router.push(ROUTES.USER_LAND.pathDyn!(user.value.tag));
}

function navigateToSettings() {
    if (!user.value) return;
    router.push(ROUTES.SETTINGS.pathDyn!(user.value.tag));
}

watch(() => route.params.tag, () => {
    user.value = null;
    fetchUserProfile();
});

onMounted(async () => {
    if (!auth.user) await auth.fetchSessionUser()
    fetchUserProfile();
});
</script>

<template>
    <div class="w-screen min-h-screen bg-slate-950 text-slate-200 pb-20">

        <div v-if="isLoading" class="flex items-center justify-center h-screen">
            <span class="loading loading-spinner text-emerald-500 loading-lg"></span>
        </div>

        <div v-else-if="user" class="animate-fade-in relative">

            <div class="relative h-64 w-full overflow-hidden">
                <div class="absolute inset-0 bg-gradient-to-b from-emerald-900/40 via-slate-900/80 to-slate-950 z-0">
                </div>
                <div class="absolute -top-20 -left-20 w-96 h-96 bg-emerald-500/10 rounded-full blur-[80px]"></div>
                <div class="absolute top-10 right-0 w-64 h-64 bg-blue-500/10 rounded-full blur-[80px]"></div>

                <div
                    class="absolute bottom-0 left-0 w-full p-6 phone:p-10 flex flex-col md:flex-row items-end md:items-center gap-6 z-10">

                    <div class="relative group">
                        <div
                            class="w-24 h-24 md:w-32 md:h-32 rounded-2xl bg-slate-800 border-4 border-slate-950 shadow-2xl flex items-center justify-center text-4xl overflow-hidden relative">
                            <span class="z-10">{{ user.tag.substring(0, 2).toUpperCase() }}</span>
                            <div class="absolute inset-0 bg-gradient-to-tr from-slate-800 to-slate-700"></div>
                        </div>
                        <div class="absolute -bottom-2 -right-2 badge badge-lg border-slate-950 font-bold shadow-lg"
                            :class="user.roles.includes(Role.ADMIN) ? 'badge-error text-white' : 'badge-primary text-slate-900'">
                            Lv. {{ user.level }}
                        </div>
                    </div>

                    <div class="flex-1 mb-2">
                        <h1 class="text-3xl md:text-5xl font-bold text-white tracking-tight flex items-center gap-3">
                            {{ user.tag }}
                            <span v-if="user.roles.includes(Role.ADMIN)" class="tooltip tooltip-right"
                                data-tip="Administrator">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                                    class="w-6 h-6 text-red-500">
                                    <path fill-rule="evenodd"
                                        d="M12.516 2.17a.75.75 0 00-1.032 0 11.209 11.209 0 01-7.877 3.08.75.75 0 00-.722.515A12.74 12.74 0 002.25 9.75c0 5.942 4.064 10.933 9.563 12.348a.749.749 0 00.374 0c5.499-1.415 9.563-6.406 9.563-12.348 0-1.352-.272-2.65-.759-3.84a.75.75 0 00-.713-.507 11.215 11.215 0 01-7.76-3.234zM9.53 9.53a.75.75 0 000 1.06l1.97 1.97l3.97-3.97a.75.75 0 10-1.06-1.06L11.5 10.44l-1.47-1.47a.75.75 0 00-1.06 0z"
                                        clip-rule="evenodd" />
                                </svg>
                            </span>
                        </h1>
                        <p class="text-slate-400 mt-1 max-w-xl text-sm md:text-base line-clamp-2">
                            {{ user.description || "No bio provided yet." }}
                        </p>
                    </div>

                    <div class="flex gap-3 w-full md:w-auto">
                        <button v-if="hasIsland" @click="navigateToLand"
                            class="btn btn-primary flex-1 md:flex-none shadow-lg shadow-emerald-900/20">
                            Visit Island
                        </button>

                        <button v-if="isOwnProfile" @click="navigateToSettings"
                            class="btn btn-outline border-slate-700 text-slate-300 hover:text-white hover:border-slate-500">
                            Edit Profile
                        </button>
                    </div>
                </div>
            </div>

            <div class="max-w-7xl mx-auto px-4 phone:px-6 py-8 grid grid-cols-1 lg:grid-cols-3 gap-8">

                <div class="space-y-6">
                    <div class="card bg-slate-900 border border-slate-800 shadow-xl overflow-hidden">
                        <div class="card-body p-6">
                            <div class="flex justify-between items-center mb-2">
                                <span
                                    class="text-xs font-bold text-slate-500 uppercase tracking-wider">Experience</span>
                                <span class="text-xs font-mono text-emerald-400">{{ user.xp }} / {{ user.level * 1000 }}
                                    XP</span>
                            </div>
                            <progress class="progress progress-success w-full bg-slate-800 h-3" :value="levelProgress"
                                max="100"></progress>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div
                            class="bg-slate-900 p-4 rounded-xl border border-slate-800 flex flex-col items-center text-center">
                            <div class="mb-2 text-emerald-500">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 18.75a60.07 60.07 0 0115.797 2.101c.727.198 1.453-.342 1.453-1.096V18.75M3.75 4.5v.75A.75.75 0 013 6h-.75m0 0v-.375c0-.621.504-1.125 1.125-1.125H20.25M2.25 6v9m18-10.5v.75c0 .414.336.75.75.75h.75m-1.5-1.5h.375c.621 0 1.125.504 1.125 1.125v9.75c0 .621-.504 1.125-1.125 1.125h-.375m1.5-1.5H21a.75.75 0 00-.75.75v.75m0 0H3.75m0 0h-.375a1.125 1.125 0 01-1.125-1.125V15m1.5 1.5v-.75A.75.75 0 003 15h-.75M15 10.5a3 3 0 11-6 0 3 3 0 016 0zm3 0h.008v.008H18V10.5zm-12 0h.008v.008H6V10.5z" />
                                </svg>
                            </div>
                            <div class="text-lg font-bold text-white font-mono">{{ user.sap.toLocaleString() }}</div>
                            <div class="text-[10px] uppercase text-slate-500 font-bold tracking-wider">Net Worth</div>
                        </div>

                        <div
                            class="bg-slate-900 p-4 rounded-xl border border-slate-800 flex flex-col items-center text-center">
                            <div class="mb-2 text-blue-500">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 6.75V15m6-6v8.25m.503 3.498l4.875-2.437c.381-.19.622-.58.622-1.006V4.82c0-.836-.88-1.38-1.628-1.006l-3.869 1.934c-.317.159-.69.159-1.006 0L9.503 3.252a1.125 1.125 0 00-1.006 0L3.622 5.689C3.24 5.88 3 6.27 3 6.695V19.18c0 .836.88 1.38 1.628 1.006l3.869-1.934c.317-.159.69-.159 1.006 0l4.994 2.497c.317.158.69.158 1.006 0z" />
                                </svg>
                            </div>
                            <div class="text-lg font-bold text-white font-mono">{{ user.maxPlots }}</div>
                            <div class="text-[10px] uppercase text-slate-500 font-bold tracking-wider">Plots Owned</div>
                        </div>

                        <div
                            class="bg-slate-900 p-4 rounded-xl border border-slate-800 flex flex-col items-center text-center">
                            <div class="mb-2 text-amber-500">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M16.5 18.75h-9m9 0a3 3 0 013 3h-15a3 3 0 013-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0V5.625a3.375 3.375 0 10-6.75 0v9.75m6.75 0h2.094a1.875 1.875 0 001.875-1.875v-9m-9 0H3.562a1.875 1.875 0 00-1.875 1.875v9" />
                                </svg>
                            </div>
                            <div class="text-lg font-bold text-white font-mono">{{ user.score }}</div>
                            <div class="text-[10px] uppercase text-slate-500 font-bold tracking-wider">Score</div>
                        </div>

                        <div
                            class="bg-slate-900 p-4 rounded-xl border border-slate-800 flex flex-col items-center text-center">
                            <div class="mb-2 text-purple-500">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5m-9-6h.008v.008H12v-.008zM12 15h.008v.008H12V15zm0 2.25h.008v.008H12v-.008zM9.75 15h.008v.008H9.75V15zm0 2.25h.008v.008H9.75v-.008zM7.5 15h.008v.008H7.5V15zm0 2.25h.008v.008H7.5v-.008zm6.75-4.5h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V15zm0 2.25h.008v.008h-.008v-.008zm2.25-4.5h.008v.008H16.5v-.008zm0 2.25h.008v.008H16.5V15z" />
                                </svg>
                            </div>
                            <div class="text-lg font-bold text-white font-mono text-sm leading-6 mt-1">{{ stats.joinedAt
                                }}</div>
                            <div class="text-[10px] uppercase text-slate-500 font-bold tracking-wider">Joined</div>
                        </div>
                    </div>
                </div>

                <div class="lg:col-span-2 space-y-8">

                    <div>
                        <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
                            <span class="w-1 h-6 bg-purple-500 rounded-full"></span>
                            Achievements
                        </h3>
                        <div class="bg-slate-900 rounded-xl border border-slate-800 p-6">

                            <div v-if="achievements.length === 0" class="text-center text-slate-500 italic py-4">
                                No achievements defined.
                            </div>

                            <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div v-for="ach in achievements" :key="ach.id"
                                    class="flex items-center gap-4 p-3 rounded-lg border transition-all" :class="ach.unlocked
                                        ? 'bg-slate-800/50 border-slate-700/50'
                                        : 'bg-slate-950/50 border-transparent opacity-50 grayscale'">
                                    <div>
                                        <div class="font-bold text-sm"
                                            :class="ach.unlocked ? 'text-white' : 'text-slate-500'">
                                            {{ ach.name }}
                                        </div>
                                        <div class="text-xs text-slate-500">{{ ach.description }}</div>
                                        <div v-if="ach.unlocked && ach.unlockedAt"
                                            class="text-[10px] text-emerald-500 mt-1">
                                            Unlocked {{ new Date(ach.unlockedAt).toLocaleDateString() }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div v-if="userInventory">
                        <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
                            <span class="w-1 h-6 bg-amber-500 rounded-full"></span>
                            Showcase
                        </h3>
                        <div
                            class="bg-slate-900 rounded-xl border border-slate-800 p-6 flex flex-col items-center justify-center text-center min-h-[200px]">

                            <div v-if="userInventory.bestFlower" class="relative group cursor-pointer perspective-1000">
                                <div
                                    class="absolute inset-0 bg-amber-500/20 rounded-full blur-2xl group-hover:bg-amber-500/30 transition-all">
                                </div>
                                <div class="relative bg-slate-950 p-6 rounded-xl border border-slate-800 shadow-2xl flex flex-col items-center gap-4 w-64 transform transition-all duration-500 group-hover:rotate-y-12 group-hover:scale-105"
                                    :class="getRarityColor(userInventory.bestFlower.rarity).split(' ')[2]">

                                    <div class="text-6xl filter drop-shadow-lg animate-float text-pink-400">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                            stroke-width="1.5" stroke="currentColor" class="w-20 h-20">
                                            <path stroke-linecap="round" stroke-linejoin="round"
                                                d="M15.362 5.214A8.252 8.252 0 0112 21 8.25 8.25 0 016.038 7.048 8.287 8.287 0 009 9.6a8.983 8.983 0 013.361-6.867 8.21 8.21 0 003 2.48z" />
                                            <path stroke-linecap="round" stroke-linejoin="round"
                                                d="M12 18a3.75 3.75 0 00.495-7.467 5.99 5.99 0 00-1.925 3.546 5.974 5.974 0 01-2.133-1A3.75 3.75 0 0012 18z" />
                                        </svg>
                                    </div>

                                    <div>
                                        <div class="font-bold text-white text-lg">{{ userInventory.bestFlower.name }}
                                        </div>
                                        <div class="badge badge-sm mt-2 border-none font-bold tracking-widest"
                                            :class="getRarityColor(userInventory.bestFlower.rarity)">
                                            {{ userInventory.bestFlower.rarity }}
                                        </div>
                                    </div>

                                    <div class="w-full h-px bg-slate-800 my-1"></div>
                                    <div class="text-xs text-slate-500">Discovered on {{ stats.joinedAt }}</div>
                                </div>
                            </div>
                            <p v-else class="text-slate-500 italic">No rare flowers discovered yet.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.perspective-1000 {
    perspective: 1000px;
}

.animate-float {
    animation: float 6s ease-in-out infinite;
}

@keyframes float {

    0%,
    100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-10px);
    }
}

.animate-fade-in {
    animation: fadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
```

---
### File: src/views/user/LoginView.vue
---

```vue
<script setup lang="ts">

</script>

<template>
    <h1>Empty View</h1>
</template>
```

---
### File: src/views/user/SettingsView.vue
---

```vue
<script setup lang="ts">

</script>

<template>
    <h1>Empty View</h1>
</template>
```

---
### File: src/views/user/SignupView.vue
---

```vue
<script setup lang="ts">

</script>

<template>
    <h1>Empty View</h1>
</template>
```

---
### File: src/views/user/SupportView.vue
---

```vue
<script setup lang="ts">
import { ref } from 'vue';
import { ReportController } from '@/server/controllers/ReportController';
import { ReportType } from '@/shared/types';
import { useAuthStore } from '@/stores/auth';

const auth = useAuthStore();

// --- STATE ---
const isSubmitting = ref(false);
const submitStatus = ref<'IDLE' | 'SUCCESS' | 'ERROR'>('IDLE');
const errorMessage = ref('');

const formData = ref({
    type: ReportType.BUG,
    title: '',
    description: ''
});

// --- CONFIG ---
const REPORT_TYPES = [
    {
        id: ReportType.BUG,
        label: 'Bug Report',
        desc: 'Glitches & Errors',
        activeClass: 'border-red-500/50 bg-red-500/10 text-red-400 ring-1 ring-red-500/50',
        iconPath: 'M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z' // Warning Triangle
    },
    {
        id: ReportType.FEATURE,
        label: 'Feature Idea',
        desc: 'Feedback & Suggestions',
        activeClass: 'border-purple-500/50 bg-purple-500/10 text-purple-400 ring-1 ring-purple-500/50',
        iconPath: 'M12 18v-5.25m0 0a6.01 6.01 0 001.5-.189m-1.5.189a6.01 6.01 0 01-1.5-.189m3.75 7.478a12.06 12.06 0 01-4.5 0m3.75 2.383a14.406 14.406 0 01-3 0M14.25 18v-.192c0-.983.658-1.823 1.508-2.316a7.5 7.5 0 10-7.517 0c.85.493 1.509 1.333 1.509 2.316V18' // Lightbulb
    },
    {
        id: ReportType.PLAYER_REPORT,
        label: 'Player Report',
        desc: 'Conduct & Abuse',
        activeClass: 'border-amber-500/50 bg-amber-500/10 text-amber-400 ring-1 ring-amber-500/50',
        iconPath: 'M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z' // Shield Check
    },
    {
        id: ReportType.OTHER,
        label: 'General Inquiry',
        desc: 'Other questions',
        activeClass: 'border-blue-500/50 bg-blue-500/10 text-blue-400 ring-1 ring-blue-500/50',
        iconPath: 'M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 01.865-.501 48.172 48.172 0 003.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z' // Chat
    },
];

const FAQS = [
    { q: 'How do I earn Sap?', a: 'Sap is earned by selling flowers to other players or completing daily objectives.' },
    { q: 'Can I move my plots?', a: 'Once a plot is purchased, it is fixed to the grid. You cannot move it, but you can change the soil type later.' },
    { q: 'I found a bug!', a: 'Please use the form on the right to report it. Include as much detail as possible.' },
];

// --- ACTIONS ---
async function submitForm() {
    if (!auth.user) {
        submitStatus.value = 'ERROR';
        errorMessage.value = 'You must be logged in to submit a ticket.';
        return;
    }

    isSubmitting.value = true;
    submitStatus.value = 'IDLE';
    errorMessage.value = '';

    try {
        await ReportController.submitReport({
            type: formData.value.type,
            title: formData.value.title,
            description: formData.value.description
        });

        submitStatus.value = 'SUCCESS';
        formData.value.title = '';
        formData.value.description = '';
        formData.value.type = ReportType.BUG;

    } catch (e: any) {
        submitStatus.value = 'ERROR';
        errorMessage.value = e.message || 'An error occurred.';
    } finally {
        isSubmitting.value = false;
    }
}
</script>

<template>
    <div class="min-h-screen bg-slate-950 text-slate-200 pt-24 pb-12 px-4 phone:px-8 relative overflow-hidden">

        <div
            class="absolute top-0 left-0 w-full h-96 bg-gradient-to-b from-slate-900 to-transparent pointer-events-none">
        </div>
        <div
            class="absolute top-20 right-0 w-[500px] h-[500px] bg-emerald-500/5 rounded-full blur-[100px] pointer-events-none">
        </div>

        <div class="max-w-7xl mx-auto relative z-10">

            <div class="text-center mb-16 animate-fade-in">
                <h1 class="text-4xl md:text-5xl font-bold text-white mb-4">Support Center</h1>
                <p class="text-slate-400 max-w-2xl mx-auto text-lg">
                    Need help with your garden? Have a suggestion for the economy?
                    Our team is here to help.
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-24 items-start">

                <div class="space-y-12 animate-slide-right">

                    <div class="p-6 rounded-2xl bg-slate-900/50 border border-slate-800 backdrop-blur-sm">
                        <h3 class="text-xl font-bold text-white mb-4">Community Channels</h3>
                        <div class="grid grid-cols-2 gap-4">
                            <a href="#"
                                class="btn btn-outline border-indigo-500/30 text-indigo-400 hover:bg-indigo-500 hover:border-indigo-500 hover:text-white gap-2">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                                    <path
                                        d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03z" />
                                </svg>
                                Discord
                            </a>
                            <a href="#"
                                class="btn btn-outline border-sky-500/30 text-sky-400 hover:bg-sky-500 hover:border-sky-500 hover:text-white gap-2">
                                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                                    <path
                                        d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z" />
                                </svg>
                                Twitter
                            </a>
                        </div>
                    </div>

                    <div>
                        <h3 class="text-xl font-bold text-white mb-6">Frequently Asked Questions</h3>
                        <div class="space-y-2">
                            <div v-for="(item, i) in FAQS" :key="i"
                                class="collapse collapse-arrow bg-slate-900 border border-slate-800 rounded-xl">
                                <input type="radio" name="my-accordion-2" :checked="i === 0" />
                                <div class="collapse-title text-sm font-medium text-slate-200">{{ item.q }}</div>
                                <div class="collapse-content text-sm text-slate-400">
                                    <p>{{ item.a }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="animate-slide-left">
                    <div
                        class="bg-slate-900 border border-slate-800 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">

                        <div v-if="submitStatus === 'SUCCESS'"
                            class="absolute inset-0 z-20 bg-slate-900 flex flex-col items-center justify-center text-center p-8 animate-fade-in">
                            <div
                                class="w-20 h-20 bg-emerald-500/20 text-emerald-400 rounded-full flex items-center justify-center mb-6">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                                    stroke="currentColor" class="w-10 h-10">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                                </svg>
                            </div>
                            <h3 class="text-2xl font-bold text-white mb-2">Report Submitted</h3>
                            <p class="text-slate-400 mb-8 max-w-sm">Thanks for your feedback. We will review it shortly.
                            </p>
                            <button @click="submitStatus = 'IDLE'"
                                class="btn btn-outline border-slate-700 text-white hover:bg-slate-800">Send
                                Another</button>
                        </div>

                        <h2 class="text-2xl font-bold text-white mb-2">Submit a Ticket</h2>
                        <p class="text-slate-500 text-sm mb-6">Select a category and describe your issue.</p>

                        <form @submit.prevent="submitForm" class="space-y-6">

                            <div class="grid grid-cols-2 gap-3">
                                <label v-for="type in REPORT_TYPES" :key="type.id"
                                    class="cursor-pointer relative group">
                                    <input type="radio" :value="type.id" v-model="formData.type" class="peer sr-only" />

                                    <div class="p-4 rounded-xl border border-slate-800 bg-slate-950/50 hover:bg-slate-800 hover:border-slate-600 transition-all duration-200 flex flex-col gap-3 h-full"
                                        :class="formData.type === type.id ? type.activeClass : 'text-slate-400'">

                                        <div
                                            class="w-8 h-8 rounded-lg bg-slate-900 border border-white/5 flex items-center justify-center shadow-sm">
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                                stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                                <path stroke-linecap="round" stroke-linejoin="round"
                                                    :d="type.iconPath" />
                                            </svg>
                                        </div>

                                        <div>
                                            <div class="text-sm font-bold"
                                                :class="formData.type === type.id ? 'text-white' : 'text-slate-300'">{{
                                                    type.label }}</div>
                                            <div class="text-[10px] opacity-70 leading-tight">{{ type.desc }}</div>
                                        </div>
                                    </div>
                                </label>
                            </div>

                            <div class="space-y-6">
                                <div class="group">
                                    <label
                                        class="block text-xs font-bold text-slate-400 uppercase tracking-wider mb-2 ml-1">
                                        Subject
                                    </label>
                                    <input type="text" v-model="formData.title" placeholder="Brief summary..."
                                        class="input w-full bg-slate-950/50 border border-slate-700/50 rounded-xl px-4 py-3 text-slate-200 placeholder:text-slate-600 focus:outline-none focus:border-emerald-500/50 focus:ring-2 focus:ring-emerald-500/20 transition-all duration-200" />
                                </div>

                                <div class="group">
                                    <label
                                        class="block text-xs font-bold text-slate-400 uppercase tracking-wider mb-2 ml-1">
                                        Description
                                    </label>
                                    <textarea v-model="formData.description" rows="5" placeholder="Provide details..."
                                        class="textarea w-full bg-slate-950/50 border border-slate-700/50 rounded-xl px-4 py-3 text-slate-200 placeholder:text-slate-600 leading-relaxed focus:outline-none focus:border-emerald-500/50 focus:ring-2 focus:ring-emerald-500/20 transition-all duration-200 resize-none"></textarea>
                                </div>
                            </div>

                            <div v-if="submitStatus === 'ERROR'"
                                class="alert alert-error text-sm py-2 rounded-lg bg-red-900/20 border border-red-500/20 text-red-400">
                                <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-5 w-5"
                                    fill="none" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <span>{{ errorMessage }}</span>
                            </div>

                            <div class="pt-2">
                                <button type="submit" :disabled="isSubmitting"
                                    class="btn btn-primary w-full text-slate-900 font-bold shadow-lg shadow-emerald-500/10 border-none hover:bg-emerald-400">
                                    <span v-if="isSubmitting" class="loading loading-spinner"></span>
                                    <span v-else>Submit Ticket</span>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.animate-fade-in {
    animation: fadeIn 0.8s ease-out forwards;
}

.animate-slide-right {
    animation: slideRight 0.6s ease-out forwards;
    opacity: 0;
    animation-delay: 0.2s;
}

.animate-slide-left {
    animation: slideLeft 0.6s ease-out forwards;
    opacity: 0;
    animation-delay: 0.4s;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideRight {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideLeft {
    from {
        opacity: 0;
        transform: translateX(30px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>
```

---
### File: tsconfig.app.json
---

```json
// tsconfig.app.json (Fichier Frontend)
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "noEmit": true,

    "module": "node20"
  },
  "include": ["src/App.vue", "src/**/*.ts", "src/**/*.vue"],
  "exclude": ["src/server/**/*.ts"]
}

```

---
### File: tsconfig.json
---

```json
{
  "references": [],
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    },
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}

```

---
### File: tsconfig.node.json
---

```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "composite": true,
    "noEmit": true
  },
  "include": ["vite.config.ts"]
}

```

---
### File: vite.config.ts
---

```ts
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), vueJsx(), vueDevTools(), tailwindcss()],
  resolve: {
    alias: {
      // Méthode moderne compatible ESM
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    port: 3001,
    proxy: {
      '/api': {
        target: 'http://localhost:3002',
        changeOrigin: true,
        secure: false,
      },
    },
  },
})

```

