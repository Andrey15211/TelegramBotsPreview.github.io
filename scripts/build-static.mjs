import { cp, mkdir, rm } from "node:fs/promises";

const outputDir = "public";

await rm(outputDir, { recursive: true, force: true });
await mkdir(outputDir, { recursive: true });

for (const path of ["index.html", "assets", "components", "webapps"]) {
  await cp(path, `${outputDir}/${path}`, { recursive: true });
}

console.log("Static files copied to public/");
