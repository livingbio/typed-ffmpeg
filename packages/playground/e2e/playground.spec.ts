import { test, expect } from '@playwright/test';

test.describe('Playground', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/typed-ffmpeg/typed-ffmpeg-playground/');
  });

  test('page loads with the flow editor and sidebar', async ({ page }) => {
    // Sidebar header
    await expect(page.getByText('FFmpeg Flow Editor').first()).toBeVisible();
    // I/O node section
    await expect(page.getByText('I/O Nodes')).toBeVisible();
    await expect(page.getByText('Input Node')).toBeVisible();
    await expect(page.getByText('Output Node')).toBeVisible();
    // Filter search
    await expect(page.getByPlaceholder('Search filters...')).toBeVisible();
  });

  test('filter search narrows the filter list', async ({ page }) => {
    const searchInput = page.getByPlaceholder('Search filters...');
    await searchInput.fill('scale');
    await expect(page.getByText('scale').first()).toBeVisible();
    // A filter that doesn't match should not appear
    await expect(page.getByText('volume').first()).not.toBeVisible();
  });

  test('clicking Input Node adds a node to the canvas', async ({ page }) => {
    // Count initial nodes (expect 1: the global node)
    const initialNodes = await page.locator('.react-flow__node').count();

    await page.getByText('Input Node').click();

    // A new node should appear
    await expect(page.locator('.react-flow__node')).toHaveCount(initialNodes + 1);
  });

  test('clicking Output Node adds a node to the canvas', async ({ page }) => {
    const initialNodes = await page.locator('.react-flow__node').count();

    await page.getByText('Output Node').click();

    await expect(page.locator('.react-flow__node')).toHaveCount(initialNodes + 1);
  });

  test('clicking a filter from the list adds it to the canvas', async ({ page }) => {
    const initialNodes = await page.locator('.react-flow__node').count();

    // Use search to find a specific filter then click it
    await page.getByPlaceholder('Search filters..').fill('scale');
    await page.getByText('scale').first().click();

    await expect(page.locator('.react-flow__node')).toHaveCount(initialNodes + 1);
  });

  test('PreviewPanel shows placeholder before graph is connected', async ({ page }) => {
    await expect(
      page.getByText(/Connect an input and output to generate a command/),
    ).toBeVisible();
  });

  test('Parse Command button is visible', async ({ page }) => {
    await expect(page.getByRole('button', { name: /Parse Command/i })).toBeVisible();
  });

  test('Copy button is initially disabled', async ({ page }) => {
    const copyBtn = page.getByRole('button', { name: 'Copy', exact: true });
    await expect(copyBtn).toBeDisabled();
  });

  test('GitHub link is present in the sidebar', async ({ page }) => {
    await expect(
      page.getByRole('link', { name: /github\.com\/livingbio\/typed-ffmpeg/ }),
    ).toBeVisible();
  });
});
