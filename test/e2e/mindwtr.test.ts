import { describe, expect, it } from 'bun:test';
import { resolve } from 'node:path';

const cli = resolve(import.meta.dir, '../../skills/mindwtr/scripts/mindwtr.mjs');

describe('mindwtr process smoke', () => {
  it('renders a valid recurring-task request without network access', () => {
    const result = Bun.spawnSync([
      'node', cli,
      '--url', 'https://mindwtr.example',
      'recurring', 'Weekly review',
      '--rule', 'weekly',
      '--strategy', 'strict',
      '--by-day', 'MO,TH',
      '--dry-run',
    ]);
    expect(result.exitCode).toBe(0);
    const payload = JSON.parse(result.stdout.toString());
    expect(payload).toMatchObject({
      dryRun: true,
      method: 'POST',
      path: '/v1/tasks',
      body: {
        title: 'Weekly review',
        props: {
          recurrence: {
            rule: 'weekly',
            strategy: 'strict',
            byDay: ['MO', 'TH'],
            rrule: 'FREQ=WEEKLY;BYDAY=MO,TH',
          },
        },
      },
    });
  });
});
