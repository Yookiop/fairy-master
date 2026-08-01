// Boss images configuration and plotting API
const CODE_CONFIGURED_BOSS_IMAGES = Object.freeze({
    //'Bryophyta': {
    //    fileName: 'Bryophyta.png',
    //    chunkIds: ['chunk_10_32']
    //},'Scurrius': {
    //    fileName: 'Scurrius.png',
    //    chunkIds: ['chunk_10_32']
    //},
    //'Obor': {
    //    fileName: 'Obor.png',
    //    chunkIds: ['chunk_10_32']
    //},
    'Lizardman Shaman': {
        fileName: 'Lizardman_shaman_temp.png',
        chunkIds: ['chunk_7_6']
    },
    'Yama': {
        fileName: 'Yama.png',
        chunkIds: ['chunk_7_6']
    }
    //,
    //'Kalphite Queen': {
    //    fileName: 'Kalphite_Queen.png',
    //    chunkIds: ['chunk_16_34']
    //},
    //'Kurask': {
    //    fileName: 'Kurask.png',
    //    chunkIds: ['chunk_8_27']
    //},
    //'Leviathan': {
    //    fileName: 'The_Leviathan.png',
    //    chunkIds: ['chunk_15_32']
    //},
    //'Thermonuclear Smoke Devil': {
    //    fileName: 'Thermonuclear_smoke_devil.png',
    //    chunkIds: ['chunk_17_21']
    //}
});

// Fairy ring locations - world map travel icons
// Data derived from RuneLite FairyRingLocation.java (WorldPoint -> chunk conversion)
const FAIRY_RING_LOCATIONS = Object.freeze({
    'CIS': { chunkId: 'chunk_4_9', dest: 'N of Arceuus Library', x: 1636, y: 3869 },
    'AJS': { chunkId: 'chunk_4_23', dest: 'Penguins near Miscellania', x: 2499, y: 3898 },
    'CIP': { chunkId: 'chunk_4_23', dest: 'Miscellania island', x: 2512, y: 3886 },
    'CIR': { chunkId: 'chunk_6_4', dest: 'NE of Farming Guild', x: 1303, y: 3762 },
    'DKS': { chunkId: 'chunk_6_26', dest: 'Polar Hunter area', x: 2743, y: 3721 },
    'DJR': { chunkId: 'chunk_7_6', dest: 'Chasm of Fire', x: 1452, y: 3659 },
    'AKQ': { chunkId: 'chunk_8_20', dest: 'Piscatoris Hunter area', x: 2318, y: 3617 },
    'ALP': { chunkId: 'chunk_8_23', dest: 'Lighthouse island', x: 2502, y: 3638 },
    'AJR': { chunkId: 'chunk_8_27', dest: 'Slayer cave', x: 2779, y: 3615 },
    'AKR': { chunkId: 'chunk_9_12', dest: 'Hosidius Vinery', x: 1823, y: 3539 },
    'CJR': { chunkId: 'chunk_9_26', dest: 'Sinclair Mansion', x: 2704, y: 3578 },
    'BLS': { chunkId: 'chunk_10_4', dest: 'S of Mount Quidamortem', x: 1293, y: 3495 },
    'ALS': { chunkId: 'chunk_10_25', dest: "McGrubor's Wood", x: 2643, y: 3497 },
    'DKR': { chunkId: 'chunk_10_32', dest: 'Edgeville, Grand Exchange', x: 3126, y: 3496 },
    'CKS': { chunkId: 'chunk_10_37', dest: 'Canifis', x: 3446, y: 3472 },
    'ALQ': { chunkId: 'chunk_10_40', dest: 'Haunted Woods E of Canifis', x: 3598, y: 3496 },
    'BKR': { chunkId: 'chunk_11_38', dest: 'Mort Myre Swamp S of Canifis', x: 3468, y: 3433 },
    'BLR': { chunkId: 'chunk_12_26', dest: "Legends' Guild", x: 2739, y: 3353 },
    'AIS': { chunkId: 'chunk_13_6', dest: 'Auburn Valley', x: 1430, y: 3323 },
    'BIS': { chunkId: 'chunk_13_25', dest: 'Ardougne Zoo - Unicorns', x: 2635, y: 3268 },
    'BIP': { chunkId: 'chunk_13_37', dest: 'Island SW of Mort Myre', x: 3409, y: 3326 },
    'DJP': { chunkId: 'chunk_14_25', dest: 'Tower of Life', x: 2657, y: 3232 },
    'AIR': { chunkId: 'chunk_14_26', dest: 'Island SE of Ardougne', x: 2699, y: 3249 },
    'CLP': { chunkId: 'chunk_14_32', dest: 'Island S of Draynor Village', x: 3081, y: 3208 },
    'DIS': { chunkId: 'chunk_15_32', dest: "Wizards' Tower", x: 3109, y: 3149 },
    'DLR': { chunkId: 'chunk_16_18', dest: 'Poison Waste S of Isafdar', x: 2212, y: 3101 },
    'CIQ': { chunkId: 'chunk_16_23', dest: 'NW of Yanille', x: 2527, y: 3129 },
    'CLS': { chunkId: 'chunk_16_25', dest: "Hazelmere's home island", x: 2681, y: 3083 },
    'DKP': { chunkId: 'chunk_16_29', dest: 'S of Musa Point', x: 2899, y: 3113 },
    'AIQ': { chunkId: 'chunk_16_30', dest: 'Mudskipper Point', x: 2995, y: 3112 },
    'BIQ': { chunkId: 'chunk_16_34', dest: 'Kalphite Hive', x: 3248, y: 3095 },
    'AJP': { chunkId: 'chunk_17_9', dest: 'Avium Savannah', x: 1648, y: 3011 },
    'BJS': { chunkId: 'chunk_17_17', dest: 'Near Zul-Andra', x: 2147, y: 3069 },
    'BKP': { chunkId: 'chunk_17_21', dest: 'South of Castle Wars', x: 2384, y: 3037 },
    'DLQ': { chunkId: 'chunk_17_37', dest: 'N of Nardah', x: 3422, y: 3018 },
    'BJP': { chunkId: 'chunk_18_19', dest: 'Isle of Souls', x: 2264, y: 2976 },
    'AKS': { chunkId: 'chunk_18_24', dest: 'Feldip Hunter area', x: 2570, y: 2958 },
    'CKR': { chunkId: 'chunk_18_27', dest: 'S of Tai Bwo Wannai', x: 2800, y: 3005 },
    'CKQ': { chunkId: 'chunk_19_5', dest: 'Aldarin', x: 1358, y: 2943 },
    'CLR': { chunkId: 'chunk_22_26', dest: 'Ape Atoll island', x: 2737, y: 2739 },
    'AKP': { chunkId: 'chunk_22_35', dest: 'Necropolis', x: 3283, y: 2704 },
    'CJQ': { chunkId: 'chunk_26_33', dest: 'The Great Conch', x: 3178, y: 2445 },
});

// Combat achievements - loaded dynamically from CSV at runtime.
// This variable is populated by loadCombatAchievementsFromCSV() before the app uses it.
let CODE_CONFIGURED_COMBAT_ACHIEVEMENTS = {};

/**
 * Parse a single CSV line that may contain quoted fields (with embedded semicolons/quotes).
 * Returns an array of field strings.
 */
function parseCSVLine(line, delimiter = ';') {
  const fields = [];
  let current = '';
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (inQuotes) {
      if (ch === '"') {
        if (i + 1 < line.length && line[i + 1] === '"') {
          current += '"'; i++; // escaped quote
        } else {
          inQuotes = false;
        }
      } else {
        current += ch;
      }
    } else {
      if (ch === '"') {
        inQuotes = true;
      } else if (ch === delimiter) {
        fields.push(current);
        current = '';
      } else {
        current += ch;
      }
    }
  }
  fields.push(current);
  return fields;
}

/**
 * Fetch Combat_Achievements.csv and build the CODE_CONFIGURED_COMBAT_ACHIEVEMENTS
 * data structure that the rest of the app expects.
 *
 * CSV columns (semicolon-delimited):
 *   0: Monster          - display name in CSV (e.g. "Theatre of Blood: Entry Mode")
 *   1: Reference        - matches CODE_CONFIGURED_BOSS_IMAGES fileName without .png
 *   2: Tier             - e.g. " Easy" (may have leading space)
 *   3: Type             - e.g. "Kill Count"
 *   4: HasSlayerReq     - "Yes" / "No"
 *   5: RequiresGroup    - "Yes" / "No"
 *   6: AchievementName  - e.g. "Hueycoatl Speed-Runner"
 *   7: Description      - free text (may contain semicolons if quoted)
 */
async function loadCombatAchievementsFromCSV() {
  // Build reverse lookup: fileName (without .png) -> { bossKey, chunkIds }
  const refToBoss = {};
  for (const [bossKey, cfg] of Object.entries(CODE_CONFIGURED_BOSS_IMAGES)) {
    const ref = cfg.fileName.replace(/\.png$/i, '');
    // Multiple boss keys may share a reference (e.g. Phosani & Nightmare both use The_Nightmare).
    // We keep the first one found - the "primary" boss is typically the shorter name / the one
    // that is also used as a key in CODE_CONFIGURED_BOSS_IMAGES.
    if (!refToBoss[ref]) {
      refToBoss[ref] = {
        bossKey,
        chunkIds: cfg.chunkIds.map(id => id.replace(/^chunk_/, ''))
      };
    }
  }

  let csvText;
  try {
    const resp = await fetch('static/Combat_Achievements.csv');
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    csvText = await resp.text();
  } catch (e) {
    console.error('Failed to load Combat_Achievements.csv:', e);
    return {};
  }

  const lines = csvText.split(/\r?\n/).filter(l => l.trim().length > 0);
  // Skip header line
  const dataLines = lines.slice(1);

  const bosses = {}; // bossKey → { chunkIds, hasSlayerRequirement, achievements[] }

  for (const line of dataLines) {
    const cols = parseCSVLine(line, ';');
    if (cols.length < 8) continue;

    const monsterName = cols[0].trim();
    const reference   = cols[1].trim();
    const tier        = cols[2].trim();
    const type        = cols[3].trim();
    const slayerReq   = cols[4].trim().toLowerCase() === 'yes';
    const groupReq    = cols[5].trim().toLowerCase() === 'yes';
    const achName     = cols[6].trim();
    // Description may span remaining columns if it contained unquoted semicolons
    const description = cols.slice(7).join(';').trim();

    if (!reference || !achName) continue;

    // Resolve which boss key this belongs to
    const mapping = refToBoss[reference];
    if (!mapping) {
      console.warn(`Combat_Achievements.csv: unknown reference "${reference}" for "${monsterName}"`);
      continue;
    }
    const bossKey = mapping.bossKey;

    // Determine if achievement name needs a mode prefix
    // e.g. "Theatre of Blood: Entry Mode" -> prefix "Entry Mode: "
    //      "Phosani's Nightmare" -> no prefix (different boss name, but not a "Mode" suffix)
    let finalName = achName;
    if (monsterName !== bossKey) {
      const colonIdx = monsterName.indexOf(': ');
      if (colonIdx >= 0) {
        const modePart = monsterName.substring(colonIdx + 2); // e.g. "Entry Mode"
        finalName = modePart + ': ' + achName;
      }
      // If no colon (e.g. "Phosani's Nightmare"), keep achievement name as-is
    }

    // Ensure boss entry exists
    if (!bosses[bossKey]) {
      bosses[bossKey] = {
        chunkIds: mapping.chunkIds,
        achievements: []
      };
    }

    // Set slayer requirement if any row for this boss says Yes
    if (slayerReq) {
      bosses[bossKey].hasSlayerRequirement = true;
    }

    // Build achievement object
    const achievement = {
      name: finalName,
      description: description,
      tier: tier,
      type: type
    };
    if (groupReq) {
      achievement.requiresGroup = true;
    }

    bosses[bossKey].achievements.push(achievement);
  }

  return Object.freeze(bosses);
}



(function(){
  // Utility to resolve chunkId to {row,col} using multiple heuristics
  function resolveChunkId(manifest, id){
    if(!id && id!==0) return null;
    if(typeof id === 'object' && id.row !== undefined && id.col !== undefined) return { row: id.row, col: id.col };
    const s = String(id).trim();
    // common formats: "r,c" or "r,c" with spaces
    if(s.indexOf(',')>=0){ const [r,c] = s.split(',').map(x=>Number(x.trim())); if(!Number.isNaN(r) && !Number.isNaN(c)) return { row:r, col:c }; }
    if(s.indexOf('.')>=0){ const [r,c] = s.split('.').map(x=>Number(x.trim())); if(!Number.isNaN(r) && !Number.isNaN(c)) return { row:r, col:c }; }
    if(s.indexOf('-')>=0){ const [r,c] = s.split('-').map(x=>Number(x.trim())); if(!Number.isNaN(r) && !Number.isNaN(c)) return { row:r, col:c }; }

    // numeric index fallback: if id is a number and fits manifest length, treat as linear index
    const n = Number(s);
    if(!Number.isNaN(n) && manifest && Array.isArray(manifest.chunks) && n>=0 && n < manifest.chunks.length){
      const ch = manifest.chunks[n]; return { row: ch.row, col: ch.col };
    }

    // try to match by looking for chunk file containing the id string
    if(manifest && Array.isArray(manifest.chunks)){
      const found = manifest.chunks.find(c => c.file && c.file.indexOf(s) >= 0);
      if(found) return { row: found.row, col: found.col };
    }

    // last attempt: if the string is 4 digits, maybe it's rrcc (two 2-digit ints)
    if(/^[0-9]{4}$/.test(s)){
      const rr = Number(s.substring(0,2)); const cc = Number(s.substring(2,4));
      if(!Number.isNaN(rr) && !Number.isNaN(cc)) return { row: rr, col: cc };
    }

    // cannot resolve
    return null;
  }

  // Create/clear markers container
  function ensureMarkersContainer(stitchedWrap){
    let c = stitchedWrap.querySelector('.boss-markers');
    if(!c){ c = document.createElement('div'); c.className = 'boss-markers'; c.style.position='absolute'; c.style.left='0'; c.style.top='0'; c.style.width='100%'; c.style.height='100%'; c.style.pointerEvents='none'; stitchedWrap.appendChild(c); }
    return c;
  }

  function clearBossMarkers(stitchedWrap){
    const c = stitchedWrap.querySelector('.boss-markers'); if(c) c.innerHTML='';
  }

  function placeBossImage(manifest, stitchedWrap, row, col, fileName, positionIndex = 0, totalCount = 1){
    // Try to use the grid info from the main window if available, to account for nudges/scaling
    const gi = window._gridInfo;
    let chunkX, chunkY, chunkW, chunkH;

    if (gi && gi.colLefts[col] !== undefined && gi.rowTops[row] !== undefined) {
        chunkX = gi.colLefts[col];
        chunkY = gi.rowTops[row];
        chunkW = gi.colWidths[col];
        chunkH = gi.rowHeights[row];
    } else {
        // Fallback to manifest bbox if grid info is not ready
        const chunk = manifest.chunks.find(ch => ch.row===row && ch.col===col);
        if(!chunk) return null;
        chunkX = chunk.bbox[0];
        chunkY = chunk.bbox[1];
        chunkW = chunk.bbox[2] - chunk.bbox[0];
        chunkH = chunk.bbox[3] - chunk.bbox[1];
    }

    const markers = ensureMarkersContainer(stitchedWrap);
    const img = document.createElement('img');
    img.src = 'static/boss_images/' + fileName;
    img.className = 'boss-marker';
    img.style.position = 'absolute';
    
    let size, offsetX, offsetY;

    if(totalCount > 6) {
        // 7-8 bosses: 3 rows layout - 3 top, 2 middle (offset), 2 bottom (offset)
        size = Math.min(chunkW, chunkH) / 3;
        const col0 = chunkX;                          // left column
        const col1 = chunkX + (chunkW - size) / 2;    // center column
        const col2 = chunkX + chunkW - size;           // right column
        const midCol0 = (col0 + col1) / 2 + size / 4; // between left & center
        const midCol1 = (col1 + col2) / 2 + size / 4; // between center & right
        const row0 = chunkY;                           // top row
        const row1 = chunkY + (chunkH - size) / 2;     // middle row
        const row2 = chunkY + chunkH - size;            // bottom row
        const positions = [
            { x: col2,    y: row0 },    // 0: top-right
            { x: col1,    y: row0 },    // 1: top-center
            { x: col0,    y: row0 },    // 2: top-left
            { x: midCol1, y: row1 },    // 3: mid-right
            { x: midCol0, y: row1 },    // 4: mid-left
            { x: midCol1, y: row2 },    // 5: bottom-right
            { x: midCol0, y: row2 },    // 6: bottom-left
            { x: col1,    y: row2 }     // 7: bottom-center (8th boss fallback)
        ];
        const pos = positions[Math.min(positionIndex, positions.length - 1)];
        offsetX = pos.x;
        offsetY = pos.y;
    } else if(totalCount === 6) {
        // 6 bosses: 3 rows layout - 3 top, 2 middle, 1 bottom-right
        // Leaves bottom-left free for the special marker icon (crown/skull)
        // 10% smaller than the 4-5 boss layout to reduce overlap
        size = Math.min(chunkW, chunkH) / 3 * 1.08;
        const col0 = chunkX;                          // left column
        const col1 = chunkX + (chunkW - size) / 2;    // center column
        const col2 = chunkX + chunkW - size;           // right column
        const midCol0 = (col0 + col1) / 2;            // between left & center
        const midCol1 = (col1 + col2) / 2;            // between center & right
        const row0 = chunkY;                           // top row
        const row1 = chunkY + (chunkH - size) / 2;     // middle row
        const row2 = chunkY + chunkH - size;            // bottom row
        const positions = [
            { x: col2,    y: row0 },    // 0 (1st): top-right
            { x: col1,    y: row0 },    // 1 (2nd): top-center
            { x: col0,    y: row0 },    // 2 (3rd): top-left
            { x: midCol1, y: row1 },    // 3 (4th): mid-right
            { x: midCol0, y: row1 },    // 4 (5th): mid-left
            { x: col2,    y: row2 }     // 5 (6th): bottom-right (leaves bottom-left for icon)
        ];
        const pos = positions[Math.min(positionIndex, positions.length - 1)];
        offsetX = pos.x;
        offsetY = pos.y;
    } else if(totalCount > 3) {
        // 4-5 bosses: top row right-to-left, bottom row right-to-left, 20% bigger than 1/3
        size = Math.min(chunkW, chunkH) / 3 * 1.2;
        const inset = (chunkH - size * 2) * 0.3; // push rows closer together (30% inset from edge)
        const positions = [
            { x: chunkX + chunkW - size,             y: chunkY + inset },                        // top-right
            { x: chunkX + (chunkW - size) / 2,       y: chunkY + inset },                        // top-center
            { x: chunkX,                              y: chunkY + inset },                        // top-left
            { x: chunkX + chunkW - size,             y: chunkY + chunkH - size - inset },         // bottom-right
            { x: chunkX + (chunkW - size) / 2,       y: chunkY + chunkH - size - inset },         // bottom-center
            { x: chunkX,                              y: chunkY + chunkH - size - inset }          // bottom-left
        ];
        const pos = positions[Math.min(positionIndex, positions.length - 1)];
        offsetX = pos.x;
        offsetY = pos.y;
    } else if(totalCount === 1) {
        // Single boss: large icon, 3/4 of chunk, top-right
        size = Math.min(chunkW, chunkH) * 0.75;
        offsetX = chunkX + (chunkW - size);
        offsetY = chunkY;
    } else {
        // 2-3 bosses: icons are 1/2 of chunk
        size = Math.min(chunkW, chunkH) / 2;
        if(positionIndex === 0) {
            // Top-Right
            offsetX = chunkX + (chunkW - size);
            offsetY = chunkY;
        } else if(positionIndex === 1) {
            // Top-Left
            offsetX = chunkX;
            offsetY = chunkY;
        } else {
            // Bottom-Right
            offsetX = chunkX + (chunkW - size);
            offsetY = chunkY + (chunkH - size);
        }
    }

    img.style.left = offsetX + 'px';
    img.style.top = offsetY + 'px';
    img.style.width = size + 'px';
    img.style.height = size + 'px';
    img.style.objectFit = 'contain';
    img.style.pointerEvents = 'none';
    // keep markers below UI panel (panel z-index is high), but above map
    img.style.zIndex = 1200;
    img.style.filter = 'drop-shadow(0 2px 4px rgba(0,0,0,0.5))';
    markers.appendChild(img);
    return img;
  }

  // Fairy ring marker helpers
  function clearFairyRingMarkers(stitchedWrap){
    const c = stitchedWrap.querySelector('.fairy-ring-markers'); if(c) c.innerHTML='';
  }

  function ensureFairyRingMarkersContainer(stitchedWrap){
    let c = stitchedWrap.querySelector('.fairy-ring-markers');
    if(!c){ c = document.createElement('div'); c.className = 'fairy-ring-markers'; c.style.position='absolute'; c.style.left='0'; c.style.top='0'; c.style.width='100%'; c.style.height='100%'; c.style.pointerEvents='none'; c.style.zIndex='1210'; stitchedWrap.appendChild(c); }
    return c;
  }

  function placeFairyRingMarker(manifest, stitchedWrap, row, col, code, positionIndex, totalCount){
    const gi = window._gridInfo;
    let chunkX, chunkY, chunkW, chunkH;
    if (gi && gi.colLefts[col] !== undefined && gi.rowTops[row] !== undefined) {
        chunkX = gi.colLefts[col]; chunkY = gi.rowTops[row]; chunkW = gi.colWidths[col]; chunkH = gi.rowHeights[row];
    } else {
        const chunk = manifest.chunks.find(ch => ch.row===row && ch.col===col);
        if(!chunk) return null;
        chunkX = chunk.bbox[0]; chunkY = chunk.bbox[1]; chunkW = chunk.bbox[2] - chunk.bbox[0]; chunkH = chunk.bbox[3] - chunk.bbox[1];
    }

    const cfg = FAIRY_RING_LOCATIONS[code];
    if(!cfg || cfg.x === undefined) return null;

    // Calculate exact pixel position from game coordinates within this chunk
    // Each chunk covers 64x64 game tiles
    const TILE_SIZE = 64;
    const MIN_X = 1024;
    const MAX_Y = 4160;
    const X_CORRECTION = -6; // fine-tune: negative = shift left, positive = shift right
    const FAIRY_RING_ICON_SHIFT_X = 27; // px, align our cyan icon ON TOP of the HD map's built-in travel icon (measured ~27px; keep in sync with index.html)
    const chunkGameX = MIN_X + col * TILE_SIZE;    // left edge of chunk in game coords
    const chunkGameY = MAX_Y - row * TILE_SIZE;     // top edge of chunk in game coords
    const fracX = (cfg.x + X_CORRECTION - chunkGameX) / TILE_SIZE; // 0..1 within chunk
    const fracY = (chunkGameY - cfg.y) / TILE_SIZE; // 0..1 within chunk

    const size = Math.min(chunkW, chunkH) * 0.135;
    let offsetX = chunkX + fracX * chunkW - size / 2 + FAIRY_RING_ICON_SHIFT_X;
    let offsetY = chunkY + fracY * chunkH - size / 2;
    
    // Constrain within chunk boundaries
    offsetX = Math.max(chunkX, Math.min(chunkX + chunkW - size, offsetX));
    offsetY = Math.max(chunkY, Math.min(chunkY + chunkH - size, offsetY));

    const container = ensureFairyRingMarkersContainer(stitchedWrap);
    
    const wrapper = document.createElement('div');
    wrapper.style.position = 'absolute';
    wrapper.style.left = offsetX + 'px';
    wrapper.style.top = offsetY + 'px';
    wrapper.style.width = size + 'px';
    wrapper.style.height = size + 'px';
    wrapper.style.pointerEvents = 'none';
    
    const dest = cfg.dest || '';
    wrapper.title = code + ': ' + dest;

    // Icon only — the blue code label on black is drawn on the grid canvas
    // (drawFairyRingChunkLabels) with a thick black leader line to this icon.
    const img = document.createElement('img');
    img.src = 'static/boss_images/fairy_ring_travel.png';
    img.className = 'fairy-ring-marker';
    img.style.width = '100%';
    img.style.height = size + 'px';
    img.style.objectFit = 'contain';
    img.style.display = 'block';
    img.style.filter = 'drop-shadow(0 1px 3px rgba(0,0,0,0.6)) brightness(1.1)';

    wrapper.appendChild(img);
    container.appendChild(wrapper);
    return wrapper;
  }

  // The public API object
  const Api = {
    tierViewMode: false, // Will be set during init
    async init(manifest, stitchedWrapArg, canvasArg, fullMapArg, tierViewMode = false){
      this.manifest = manifest; this.stitchedWrap = stitchedWrapArg; this.canvas = canvasArg; this.fullMap = fullMapArg;
      this.tierViewMode = tierViewMode;

      // Load combat achievements from CSV before rendering anything
      CODE_CONFIGURED_COMBAT_ACHIEVEMENTS = await loadCombatAchievementsFromCSV();
      
      // Automatically plot configured bosses
      this.plotConfiguredBosses();
      
      // Plot fairy ring travel icons (with small delay to ensure grid info is ready)
      setTimeout(() => this.plotFairyRings(), 100);
      
      // Initialize combat achievements panel
      this.initCombatAchievements();
    },
    plotConfiguredBosses(){
        if(!this.manifest || !this.stitchedWrap) return;
        
        // Determine which tiers are active (for filtering bosses)
        const activeTiers = this.tierViewMode && window.CURRENT_TIERS && window.CURRENT_TIERS.length > 0
          ? window.CURRENT_TIERS.map(t => t.toLowerCase())
          : (this.tierViewMode && window.CURRENT_TIER ? [window.CURRENT_TIER.toLowerCase()] : null);
        
        // Slayer/Group filter flags
        const hideSlayer = !!this.hideSlayerReq;
        const hideGroup  = !!this.hideGroupReq;
        
        // Build two sets:
        // allowedBossKeys - bosses with incomplete achievements (show everywhere)
        // completedBossKeys - bosses with ALL achievements completed (show only in unlocked chunks)
        let allowedBossKeys = new Set();
        let completedBossKeys = new Set();
        
        if(activeTiers){
          for(const [key, config] of Object.entries(CODE_CONFIGURED_COMBAT_ACHIEVEMENTS)){
            // Skip entire boss if it requires slayer and filter is active
            if(hideSlayer && config.hasSlayerRequirement) continue;
            
            let tierAchievements = config.achievements
              .map((a, idx) => ({ ...a, originalIndex: idx }))
              .filter(a => activeTiers.includes(a.tier.toLowerCase()));
            
            // Filter out group-required achievements if filter is active
            if(hideGroup) tierAchievements = tierAchievements.filter(a => !a.requiresGroup);
            
            if(tierAchievements.length === 0) continue;
            // Check if all tier-relevant achievements are completed
            const allCompleted = tierAchievements.every(a => {
              const achievementId = `${key}_${a.originalIndex}`;
              return this.completedAchievements && this.completedAchievements.has(achievementId);
            });
            if(allCompleted) completedBossKeys.add(key);
            else allowedBossKeys.add(key);
          }
        } else {
          // Normal mode (no tier filter)
          for(const [key, config] of Object.entries(CODE_CONFIGURED_COMBAT_ACHIEVEMENTS)){
            // Skip entire boss if it requires slayer and filter is active
            if(hideSlayer && config.hasSlayerRequirement) continue;
            
            let achievements = config.achievements.map((a, idx) => ({ ...a, originalIndex: idx }));
            
            // Filter out group-required achievements if filter is active
            if(hideGroup) achievements = achievements.filter(a => !a.requiresGroup);
            
            if(achievements.length === 0) continue;
            
            const allCompleted = achievements.every((a) => {
              const achievementId = `${key}_${a.originalIndex}`;
              return this.completedAchievements && this.completedAchievements.has(achievementId);
            });
            if(allCompleted) completedBossKeys.add(key);
            else allowedBossKeys.add(key);
          }
          // Also include bosses without any combat achievements
          for(const key of Object.keys(CODE_CONFIGURED_BOSS_IMAGES)){
            if(!CODE_CONFIGURED_COMBAT_ACHIEVEMENTS[key]) allowedBossKeys.add(key);
          }
        }
        
        // Get unlocked chunks for completed-boss visibility check
        const unlockedChunks = window.unlocked || new Set();
        
        // Collect bosses per chunk
        const chunkBosses = new Map(); // key: "row,col", value: [fileName, fileName...]

        for(const key of Object.keys(CODE_CONFIGURED_BOSS_IMAGES)){
            const isAllowed = allowedBossKeys.has(key);
            const isCompleted = completedBossKeys.has(key);
            // Skip bosses that are neither allowed nor completed
            if(!isAllowed && !isCompleted) continue;
            
            const cfg = CODE_CONFIGURED_BOSS_IMAGES[key];
            for(const cid of cfg.chunkIds){
                const rc = resolveChunkId(this.manifest, cid);
                if(rc){
                    const k = `${rc.row},${rc.col}`;
                    // Completed bosses only show in unlocked chunks
                    if(isCompleted && !isAllowed && !unlockedChunks.has(k)) continue;
                    if(!chunkBosses.has(k)) chunkBosses.set(k, []);
                    chunkBosses.get(k).push(cfg.fileName);
                }
            }
        }

        // Plot them
        for(const [key, fileNames] of chunkBosses.entries()){
            const [r, c] = key.split(',').map(Number);
            fileNames.forEach((fileName, index) => {
                placeBossImage(this.manifest, this.stitchedWrap, r, c, fileName, index, fileNames.length);
            });
        }
    },
    // programmatically plot a boss by config key onto a single chunk id (string) or row/col object
    plotByKeyAndChunk(key, chunkIdOrObj){
      if(!this.manifest || !this.stitchedWrap) return;
      const cfg = CODE_CONFIGURED_BOSS_IMAGES[key]; if(!cfg) return false;
      let rc = null;
      if(typeof chunkIdOrObj === 'string' || typeof chunkIdOrObj === 'number') rc = resolveChunkId(this.manifest, chunkIdOrObj);
      else if(typeof chunkIdOrObj === 'object') rc = { row: chunkIdOrObj.row, col: chunkIdOrObj.col };
      if(!rc) return false;
      placeBossImage(this.manifest, this.stitchedWrap, rc.row, rc.col, cfg.fileName);
      return true;
    },
    clear(){ if(this.stitchedWrap){ clearBossMarkers(this.stitchedWrap); clearFairyRingMarkers(this.stitchedWrap); } },
    plotFairyRings(){
        if(!this.manifest || !this.stitchedWrap) return;
        clearFairyRingMarkers(this.stitchedWrap);
        const chunkFairyRings = new Map();
        for(const [code, cfg] of Object.entries(FAIRY_RING_LOCATIONS)){
            const rc = resolveChunkId(this.manifest, cfg.chunkId);
            if(rc){
                const k = `${rc.row},${rc.col}`;
                if(!chunkFairyRings.has(k)) chunkFairyRings.set(k, []);
                chunkFairyRings.get(k).push(code);
            }
        }
        for(const [key, codes] of chunkFairyRings.entries()){
            const [r, c] = key.split(',').map(Number);
            codes.forEach((code, index) => {
                placeFairyRingMarker(this.manifest, this.stitchedWrap, r, c, code, index, codes.length);
            });
        }
    },
    
    // Combat achievements functionality
    initCombatAchievements(){
      this.loadCompletedAchievements();
      this.createCombatAchievementsPanel();
      this.updateCombatAchievements();
    },
    
    createCombatAchievementsPanel(){
      // Check if panel already exists
      if(document.getElementById('combatAchievementsPanel')) return;
      
      const panel = document.createElement('div');
      panel.id = 'combatAchievementsPanel';
      panel.className = 'combat-achievements-panel';
      
      // Build header
      const hideCompleted = localStorage.getItem('combat_hide_completed') === '1';
      let headerHtml = `
          <div class="panel-header" style="display: flex; align-items: center; justify-content: space-between;">
            <div class="panel-title">Combat achievements</div>
            <span id="toggleCompletedBtn" title="${hideCompleted ? 'Show completed tasks' : 'Hide completed tasks'}" style="cursor:pointer; font-size:16px; font-weight:bold; line-height:1; user-select:none; color:#aaa;">${hideCompleted ? '▼' : '▲'}</span>
          </div>
        `;
      
      panel.innerHTML = headerHtml + `
        <div id="combatAchievementsList" class="achievements-list">
          <div class="no-achievements">No combat achievements available for current chunks</div>
        </div>
      `;
      
      // Apply initial hide-completed state
      if(hideCompleted) panel.classList.add('hide-completed');
      
      // Wire toggle button
      const toggleBtn = panel.querySelector('#toggleCompletedBtn');
      if(toggleBtn){
        toggleBtn.addEventListener('click', () => {
          const isHidden = panel.classList.toggle('hide-completed');
          localStorage.setItem('combat_hide_completed', isHidden ? '1' : '0');
          toggleBtn.textContent = isHidden ? '▼' : '▲';
          toggleBtn.title = isHidden ? 'Show completed tasks' : 'Hide completed tasks';
        });
      }
      
      document.body.appendChild(panel);
    },
    
    updateCombatAchievements(){
      const panel = document.getElementById('combatAchievementsPanel');
      const list = document.getElementById('combatAchievementsList');
      if(!panel || !list) return;
      
      // Get only unlocked chunks
      const currentChunks = new Set();
      if(window.unlocked) {
        for(const key of window.unlocked) currentChunks.add(key);
      }
      
      // Determine which tiers to filter by (if in tier mode)
      const currentTiers = this.tierViewMode && window.CURRENT_TIERS && window.CURRENT_TIERS.length > 0
        ? window.CURRENT_TIERS.map(t => t.toLowerCase())
        : (this.tierViewMode && window.CURRENT_TIER ? [window.CURRENT_TIER.toLowerCase()] : null);
      
      // Find achievements grouped by category, filtered by current tiers if applicable
      const hideSlayer = !!this.hideSlayerReq;
      const hideGroup  = !!this.hideGroupReq;
      
      const categoriesWithAchievements = {};
      for(const [key, config] of Object.entries(CODE_CONFIGURED_COMBAT_ACHIEVEMENTS)){
        // Skip entire boss if it requires slayer and filter is active
        if(hideSlayer && config.hasSlayerRequirement) continue;
        
        for(const chunkId of config.chunkIds){
          const rc = resolveChunkId(this.manifest, chunkId);
          if(rc && currentChunks.has(`${rc.row},${rc.col}`)){
            // Filter achievements by tiers if in tier mode, but keep original index for ID
            let filteredAchievements = config.achievements.map((a, idx) => ({...a, originalIndex: idx}));
            if(currentTiers){
              filteredAchievements = filteredAchievements.filter(a => currentTiers.includes(a.tier.toLowerCase()));
            }
            // Filter out group-required achievements if filter is active
            if(hideGroup){
              filteredAchievements = filteredAchievements.filter(a => !a.requiresGroup);
            }
            
            if(filteredAchievements.length > 0){
              categoriesWithAchievements[key] = {
                name: key.charAt(0).toUpperCase() + key.slice(1),
                achievements: filteredAchievements
              };
            }
            break; // Don't add duplicates if multiple chunk IDs match
          }
        }
      }
      
      if(Object.keys(categoriesWithAchievements).length === 0){
        const tierText = currentTiers ? ` for ${currentTiers.map(t => t.charAt(0).toUpperCase()+t.slice(1)).join(', ')} tier${currentTiers.length>1?'s':''}` : '';
        list.innerHTML = `<div class="no-achievements">No combat achievements available${tierText} for current chunks</div>`;
        return;
      }
      
      // Build HTML - in tier mode with a selected tier, we group by boss
      // In normal mode without tier selection, we also group by boss
      // (The old buildTierViewHtml is no longer used since we now select a tier upfront)
      let html = this.buildCategoryViewHtml(categoriesWithAchievements);
      
      list.innerHTML = html;
      
      // Add click handlers for collapsible headers (both category and tier)
      list.querySelectorAll('.category-header, .tier-header').forEach(header => {
        header.addEventListener('click', (e) => {
          const categoryKey = e.currentTarget.dataset.category;
          const tierKey = e.currentTarget.dataset.tier;
          if(categoryKey) this.toggleCategory(categoryKey);
          if(tierKey) this.toggleTier(tierKey);
        });
      });
      
      // Add click handlers for achievement checkboxes
      list.querySelectorAll('.achievement-check').forEach(checkbox => {
        checkbox.addEventListener('change', (e) => {
          const achievementId = e.target.dataset.achievement;
          this.toggleAchievementCompletion(achievementId, e.target.checked);
        });
      });
    },
    
    buildCategoryViewHtml(categoriesWithAchievements){
      // Tier difficulty order for sorting: easy (0) -> medium (1) -> hard (2) -> elite (3) -> master (4) -> grandmaster (5)
      const tierSortOrder = { 'easy': 0, 'medium': 1, 'hard': 2, 'elite': 3, 'master': 4, 'grandmaster': 5 };
      let html = '';
      for(const [categoryKey, categoryData] of Object.entries(categoriesWithAchievements)){
        // Sort achievements by tier difficulty (easy first, grandmaster last)
        const sortedAchievements = [...categoryData.achievements].sort((a, b) => {
          const tierA = tierSortOrder[a.tier.toLowerCase()] ?? 99;
          const tierB = tierSortOrder[b.tier.toLowerCase()] ?? 99;
          return tierA - tierB;
        });
        // Count uncompleted achievements
        let uncompletedCount = 0;
        sortedAchievements.forEach((achievement) => {
          const idx = achievement.originalIndex !== undefined ? achievement.originalIndex : categoryData.achievements.indexOf(achievement);
          const achievementId = `${categoryKey}_${idx}`;
          const isCompleted = this.completedAchievements?.has(achievementId) ?? false;
          if(!isCompleted) uncompletedCount++;
        });
        
        const isExpanded = this.expandedCategories?.has(categoryKey) ?? true; // Default to expanded
        
        html += `<div class="category-section${uncompletedCount === 0 ? ' all-completed' : ''}">`;
        html += `<div class="category-header" data-category="${categoryKey}">`;
        html += `<span class="category-arrow ${isExpanded ? 'expanded' : ''}">▼</span>`;
        html += `<span class="category-name">${categoryData.name}</span>`;
        html += `<span class="category-count">(${uncompletedCount})</span>`;
        html += `</div>`;
        
        if(isExpanded) {
          html += `<div class="category-achievements">`;
          sortedAchievements.forEach((achievement) => {
            const idx = achievement.originalIndex !== undefined ? achievement.originalIndex : categoryData.achievements.indexOf(achievement);
            const achievementId = `${categoryKey}_${idx}`;
            const isCompleted = this.completedAchievements?.has(achievementId) ?? false;
            
            html += `<div class="achievement-item ${isCompleted ? 'completed' : ''}">`;
            html += `<div class="achievement-checkbox">`;
            html += `<input type="checkbox" class="achievement-check" data-achievement="${achievementId}" ${isCompleted ? 'checked' : ''}>`;
            html += `</div>`;
            html += `<div class="achievement-content">`;
            html += `<div class="achievement-name">${achievement.name}</div>`;
            html += `<div class="achievement-description">${achievement.description}</div>`;
            html += `</div>`;
            // Show tier badge: always when multiple tiers selected, or when not in tier mode
            const activeTierCount = (window.CURRENT_TIERS && window.CURRENT_TIERS.length) || (window.CURRENT_TIER ? 1 : 0);
            if(!this.tierViewMode || activeTierCount !== 1){
              html += `<div class="achievement-tier-badge tier-${achievement.tier.toLowerCase()}">${achievement.tier.toUpperCase()}</div>`;
            }
            html += `</div>`;
          });
          html += `</div>`;
        }
        
        html += `</div>`;
      }
      return html;
    },
    
    buildTierViewHtml(categoriesWithAchievements){
      // Define tier order
      const tierOrder = ['easy', 'medium', 'hard', 'elite', 'master', 'grandmaster'];
      const tierNames = {
        'easy': 'Easy',
        'medium': 'Medium', 
        'hard': 'Hard',
        'elite': 'Elite',
        'master': 'Master',
        'grandmaster': 'Grandmaster'
      };
      
      // Collect all achievements grouped by tier
      const tierAchievements = {};
      for(const tier of tierOrder) tierAchievements[tier] = [];
      
      for(const [categoryKey, categoryData] of Object.entries(categoriesWithAchievements)){
        categoryData.achievements.forEach((achievement) => {
          const tierKey = achievement.tier.toLowerCase();
          const idx = achievement.originalIndex !== undefined ? achievement.originalIndex : categoryData.achievements.indexOf(achievement);
          if(tierAchievements[tierKey]){
            tierAchievements[tierKey].push({
              ...achievement,
              categoryKey,
              achievementId: `${categoryKey}_${idx}`,
              categoryName: categoryData.name
            });
          }
        });
      }
      
      let html = '';
      
      for(const tier of tierOrder){
        const achievements = tierAchievements[tier];
        if(achievements.length === 0) continue; // Skip empty tiers
        
        // Count uncompleted achievements in this tier
        let uncompletedCount = 0;
        achievements.forEach(achievement => {
          const isCompleted = this.completedAchievements?.has(achievement.achievementId) ?? false;
          if(!isCompleted) uncompletedCount++;
        });
        
        const isExpanded = this.expandedTiers?.has(tier) ?? true; // Default to expanded
        
        html += `<div class="tier-section${uncompletedCount === 0 ? ' all-completed' : ''}">`;
        html += `<div class="tier-header tier-header-${tier}" data-tier="${tier}">`;
        html += `<span class="tier-arrow ${isExpanded ? 'expanded' : ''}">▼</span>`;
        html += `<span class="tier-name">${tierNames[tier]}</span>`;
        html += `<span class="tier-count">(${uncompletedCount})</span>`;
        html += `</div>`;
        
        if(isExpanded) {
          html += `<div class="tier-achievements">`;
          achievements.forEach(achievement => {
            const isCompleted = this.completedAchievements?.has(achievement.achievementId) ?? false;
            
            html += `<div class="achievement-item ${isCompleted ? 'completed' : ''}">`;
            html += `<div class="achievement-checkbox">`;
            html += `<input type="checkbox" class="achievement-check" data-achievement="${achievement.achievementId}" ${isCompleted ? 'checked' : ''}>`;
            html += `</div>`;
            html += `<div class="achievement-content">`;
            html += `<div class="achievement-name">${achievement.name}</div>`;
            html += `<div class="achievement-description">${achievement.description}</div>`;
            html += `<div style="font-size: 0.75rem; color: #888; margin-top: 2px;">${achievement.categoryName}</div>`;
            html += `</div>`;
            html += `</div>`;
          });
          html += `</div>`;
        }
        
        html += `</div>`;
      }
      
      return html;
    },
    
    toggleTier(tierKey){
      if(!this.expandedTiers) this.expandedTiers = new Set(['easy', 'medium', 'hard', 'elite', 'master', 'grandmaster']); // Default expanded
      
      if(this.expandedTiers.has(tierKey)){
        this.expandedTiers.delete(tierKey);
      } else {
        this.expandedTiers.add(tierKey);
      }
      
      this.updateCombatAchievements(); // Refresh the display
    },
    
    toggleCategory(categoryKey){
      if(!this.expandedCategories) this.expandedCategories = new Set(['Obor', 'Barrows']); // Default expanded
      
      if(this.expandedCategories.has(categoryKey)){
        this.expandedCategories.delete(categoryKey);
      } else {
        this.expandedCategories.add(categoryKey);
      }
      
      this.updateCombatAchievements(); // Refresh the display
    },
    
    toggleAchievementCompletion(achievementId, isCompleted){
      if(!this.completedAchievements) this.completedAchievements = new Set();
      
      if(isCompleted){
        this.completedAchievements.add(achievementId);
      } else {
        this.completedAchievements.delete(achievementId);
      }
      
      // Save to localStorage
      this.saveCompletedAchievements();
      
      // Update the visual state immediately
      this.updateCombatAchievements();
      
      // Re-plot boss images (completed bosses get hidden)
      this.clear();
      this.plotConfiguredBosses();
    },
    
    clearCompletedAchievements(){
      this.completedAchievements = new Set();
      try{ localStorage.removeItem('combat_achievements_completed'); } catch(e){}
      this.updateCombatAchievements();
      this.clear();
      this.plotConfiguredBosses();
    },

    saveCompletedAchievements(){
      try{
        const completed = Array.from(this.completedAchievements || []);
        localStorage.setItem('combat_achievements_completed', JSON.stringify(completed));
      } catch(e){
        console.warn('Failed to save completed achievements', e);
      }
    },
    
    loadCompletedAchievements(){
      try{
        const saved = localStorage.getItem('combat_achievements_completed');
        if(saved){
          const completed = JSON.parse(saved);
          this.completedAchievements = new Set(completed);
        }
      } catch(e){
        console.warn('Failed to load completed achievements', e);
        this.completedAchievements = new Set();
      }
    }
  };

  // expose globally so index.html inline script can call Api.init after loading manifest
  window.BossPickerAPI = Api;

  // small CSS injection for boss markers and fairy ring markers
  const style = document.createElement('style');
  style.textContent = `
    .boss-markers{ z-index: 1190; }
    .boss-markers img.boss-marker{ z-index: 1200; image-rendering: -webkit-optimize-contrast; will-change: transform, opacity, filter; transition: transform 220ms cubic-bezier(.21,.88,.35,1), opacity 200ms ease; }
    .fairy-ring-markers{ z-index: 1210; }
    .fairy-ring-markers img.fairy-ring-marker{ z-index: 1210; image-rendering: auto; will-change: transform; transition: transform 180ms ease; }
    .fairy-ring-markers img.fairy-ring-marker:hover{ transform: scale(1.2); z-index: 1220; }
    /* Rolling cloud overlays for selected purple chunks */
    .rolling-cloud{ position:absolute; pointer-events:none; z-index:1185; transform-origin:center; will-change: transform, opacity, filter; }
    .rolling-cloud::after{ content:''; display:block; width:100%; height:100%; border-radius:50%; background: radial-gradient(circle at 40% 40%, rgba(160,64,255,0.24) 0%, rgba(160,64,255,0.12) 40%, rgba(160,64,255,0.02) 75%, rgba(160,64,255,0) 100%); filter: blur(16px); }
    .rolling-cloud.pulse{ animation: cloudPulse var(--cloud-duration, 2600ms) ease-in-out infinite, cloudDrift var(--cloud-duration, 2600ms) linear infinite; opacity:1; }
    @keyframes cloudPulse{ 0%{ transform:scale(0.88); opacity:0.6;} 50%{ transform:scale(1); opacity:1;} 100%{ transform:scale(0.88); opacity:0.6;} }
    @keyframes cloudDrift{ 0%{ transform:translate(0,0);} 50%{ transform:translate(6px,-4px);} 100%{ transform:translate(0,0);} }
    /* ensure UI panel stays on top */
    .panel{ z-index: 100000 !important; }
  `;
  document.head.appendChild(style);
  // SVG overlay CSS removed; canvas approach used for selection, glow, and clouds
})();
