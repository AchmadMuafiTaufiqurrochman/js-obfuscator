const obfuscator = require('javascript-obfuscator');
const fs = require('fs');

const inputFile = process.argv[2];
const outputFile = process.argv[3];

const jsCode = fs.readFileSync(inputFile, 'utf-8');
const obfuscatedCode = obfuscator.obfuscate(jsCode, {
    compact: true,
    controlFlowFlattening: true,
    deadCodeInjection: true,
    debugProtection: true,
    selfDefending: true
}).getObfuscatedCode();

fs.writeFileSync(outputFile, obfuscatedCode);
